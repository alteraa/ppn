Kodu inceledikten sonra bu projenin mimari özeti şu: mikrofon → AEC/NS → VAD → ASR (OpenAI) → LLM streaming (OpenAI) → cümle cümle TTS (OpenAI) → playback, üzerinde barge‑in ve event bus telemetrisiyle. Dolayısıyla "performans" burada çoğunlukla **uçtan uca gecikme (latency)** demek; throughput ikinci planda.

Aşağıda **en etkiliden en az etkiliye** doğru, somut dosya/satır referanslarıyla sıralanmış öneriler var.

---

## 1. İlk-ses gecikmesini (time‑to‑first‑audio) kısaltmak — en kritik kazanım

Kullanıcı "konuştum → ilk kelimeyi duydum" arasındaki süre = ASR + LLM'in ilk token'ı + ilk TTS cümlesi. Bugün en büyük sabit maliyet ilk TTS segmentinin boyutu.

- `StreamingLlmPolicy.run` içinde `min_tts_segment_chars / target_tts_segment_chars` ile tetikleniyor:

```60:87:src/ar_voice_controller/core/policy.py
ready_partials, sentence_buffer = drain_partial_tts_segments(
    sentence_buffer,
    min_chars=self.settings.llm.min_tts_segment_chars,
    target_chars=self.settings.llm.target_tts_segment_chars,
    max_chars=self.settings.llm.max_tts_segment_chars,
)
```

İlk segment için eşikleri çok daha agresif tutmak (ör. ilk segment `min_chars≈12–20`, sonrakiler için mevcut değerler) tek başına algılanan gecikmeyi 300–800 ms düşürür. "Warm‑up" hissi için ilk token geldiği an kısa bir "prosody filler" (ör. "hmm…", "tabii,") TTS'e verilip arka planda gerçek cevap hazırlanabilir.

- LLM isteğinde `stream_options={"include_usage": False}` zaten default; ama `max_tokens`'ı makul bir tavana koymak (ör. 200–300) p99 latency'i düzeltir.
- ASR bitince LLM'e geçerken zaman kaybı yok ama `AsrProcessingWorker._loop` şu an **senkron çalışıyor**; ASR tamamlanmadan LLM başlamıyor:

```55:94:src/ar_voice_controller/core/worker.py
transcription = self._asr_client.transcribe(wav_bytes, token=token)
...
result = self._policy.run(
    TurnContext(turn_id=turn_id, token=token, transcript=final)
)
```

Bu kısmı değiştiremezsiniz çünkü LLM, transcript metnini bekliyor — ama **streaming ASR** (OpenAI `gpt-4o-transcribe` veya Whisper + partials) kullanılabilirse, son kelime gelmeden LLM'e "speculative prefill" gönderip VAD silence anında final tamamlayabilirsiniz (gelişmiş ama en büyük etkilerden biri).

## 2. VAD'ı hot path'ten çıkar / optimize et

Şu an **her ses chunk'ı** için Torch forward çağrısı var ve ayrıca `CaptureController.on_idle_chunk` içinde **bir kez daha** `self._vad.confidence(raw)` çağırıyorsunuz:

```82:88:src/ar_voice_controller/core/capture.py
baseline = self._detector.current_baseline()
vad_conf = self._vad.confidence(raw)
if is_speech_start(
    raw,
    baseline=baseline,
    vad_confidence=vad_conf,
```

Aynı şekilde `InterruptDetector.update` içinde de `self.vad_confidence(audio_chunk)` çağrılıyor — yani SPEAKING sırasında bazı chunk'larda VAD iki kez çalışabiliyor. Ek olarak `VadDetector.confidence` her çağrıda `np.frombuffer → astype(float32) → peak bölme → torch.from_numpy → unsqueeze` yapıyor.

Önerilen iyileştirmeler (etki: CPU %10–30 düşüşü, her iterasyonda ~2–5 ms):

1. **Chunk başına tek VAD çağrısı**: sonucu `TurnManager.run()` içinde hesaplayıp hem `capture`'a hem `interrupt_detector`'a parametre olarak geç. Mevcut tasarımda `InterruptDetector` bir callback tutuyor (`vad_confidence`) — bunu "önceden hesaplanmış değer" almaya çevir.
2. **Frame boyutunu VAD'ın beklediği 512 örnekle tam olarak eşle** (`num_samples = 512` @ 16 kHz). Şu an `confidence()` içindeki padding/splitting dalı (satır 64–83) aslında yeniden şekillendirmek zorunda; bu dal, gereksiz CPU:

```64:83:src/ar_voice_controller/audio/vad.py
n = int(math.ceil(length / expected)) if expected > 0 else 0
...
confidences.append(float(model(seg, self.sample_rate).item()))
```
3. **Tensor reuse**: `torch.from_numpy(audio_float).float().unsqueeze(0)` yerine önceden ayrılmış pinned buffer + in-place doldurma. PyTorch overhead'i çağrı başına 0.5–1 ms azalır.
4. **`torch.set_num_threads(1)`** (tek-chunk inference için daha düşük latency ve daha az context switch).
5. **ONNX Runtime ile Silero**: resmi silero-vad `silero_vad.onnx` dosyası var; `onnxruntime` CPU backend genelde 2–4x daha hızlı ve GIL dışına çıkıyor.

## 3. AEC chunk boyutu ve tahsisleri

`AecProcessor.process` her chunk'ı `aec_frame_size`'a (tipik 10 ms = 160 sample) bölüyor; mikrofondan gelen chunk'lar daha büyük olduğu için her sefer listeye parça topluyor ve **her parça için `tobytes()` + `frombuffer` + `copy()` + `concatenate`** yapıyor:

```33:54:src/ar_voice_controller/audio/aec.py
out_parts: list[np.ndarray] = []
frame_size = self._config.aec_frame_size
for start in range(0, len(mic_chunk), frame_size):
    ...
    self._processor.process_reverse_stream(ref_frame.astype(np.int16).tobytes())
    cleaned = self._processor.process_stream(mic_frame.astype(np.int16).tobytes())
    cleaned_arr = np.frombuffer(cleaned, dtype=np.int16).copy()
    out_parts.append(cleaned_arr[:valid_len])
```

Buna ek olarak `_callback` içinde `np.ascontiguousarray(indata[:,0].copy(), dtype=np.int16)` ve ardından `cleaned.astype(np.int16).tobytes()` — callback sounddevice'ın real‑time audio thread'inde çalıştığı için her mikrosaniye önemli.

Öneriler:

- Ses chunk boyutunu AEC frame boyutunun **katı** olacak şekilde ayarla ki son padding kolu hiç çalışmasın.
- Çıktı için önceden tahsisli `out = np.empty_like(mic_chunk)` kullanıp parçaları içine yerleştir; `concatenate` yok.
- `indata.copy()` yerine `indata[:,0]` zaten contiguous ise kopya atlanabilir (sounddevice'ın block buffer'ı yeniden kullanılmaz, bu yüzden kopya gerekli olabilir — ama tek kopya yeterli, sonra ayrı `.astype` yapılmasın).
- `tobytes()`/`frombuffer` döngüsü yerine AEC kütüphanesi `numpy` arayüzü sunuyorsa onu kullan.

Audio callback'te 1–2 ms tasarruf, glitch‑free çalışma payını ciddi artırır.

## 4. Event bus ve JSON telemetri

Her state değişimi, her TTS frame'i ve her LLM delta'sı `InProcessBus.publish` üzerinden gidiyor; spy olarak FifoSink her event için JSON üretiyor:

```163:169:src/ar_voice_controller/runtime/event_types.py
return json.dumps(
    {"__type__": type(event).__name__, "data": asdict(event)},
    default=str,
)
```

`TtsAudioFrame` ve `LlmTextDelta` gibi *yüksek frekanslı* event'ler çok — her biri için `asdict` (recursive copy) + `json.dumps` (stdlib, saf Python) çalışıyor. TTSPlayer ayrıca her frame için np.sqrt(mean(x**2)) hesaplıyor (`_playback_loop`, satır 168).

Öneriler:

1. **Topic filtering spy**: FifoSink yüksek frekans topic'lerini (`/tts/audio_frame`, `/llm/text_delta`) ya drop'la ya da batch'le.
2. `orjson` veya `msgspec` kullanmak `json.dumps`'ı **5–10x** hızlandırır; dataclass → dict dönüşümünü `msgspec.Struct`'la elemek de büyük kazanç.
3. `_Subscription._run` timeout=0.1 ile polling yapıyor — yüksek frekanslı handler'larda CPU wake'leri fazla; `queue.get(block=True)` yeterli, close için sentinel kullanın:

```64:69:src/ar_voice_controller/runtime/events.py
while not self._closed.is_set():
    try:
        topic, event = self._queue.get(timeout=0.1)
    except queue.Empty:
        continue
```
4. `TtsAudioFrame.rms` hesabını kapat (kimse dinlemiyorsa) veya integer domain'de yap: `int(np.sqrt((ref.astype(np.int32) * ref).mean()))`.

## 5. TTS pipeline paralelizasyonu

Şu an tek `_synthesis_worker` thread'i var:

```47:53:src/ar_voice_controller/providers/tts_player.py
self._synthesis_worker = threading.Thread(
    target=self._synthesis_loop, daemon=True
)
self._playback_worker = threading.Thread(target=self._playback_loop, daemon=True)
```

Yani segment N çalarken bile segment N+1'in sentezi seri ilerliyor. OpenAI TTS çağrıları 200–600 ms; ilk segmentten sonraki segmentleri **iki worker thread ile** paralel sentezlemek (sıralama için segment_index kullanıp playback kuyruğunu sort buffered doldurmak) ortalama yanıt süresini kısaltır. Ayrıca:

- `OpenAiTtsClient.synthesize` içinde `_resample_to_output_rate` saf Python+numpy; sample rate zaten eşitse return erken — iyi. Ama eşit değilse `np.interp` pahalı; `scipy.signal.resample_poly` ya da `soxr` ile 3–5x hızlanır.

```41:62:src/ar_voice_controller/providers/tts.py
source_positions = np.arange(len(samples), dtype=np.float32)
target_length = max(
...
resampled = np.interp(
    target_positions, source_positions, samples.astype(np.float32)
)
return np.clip(np.round(resampled), -32768, 32767).astype(np.int16)
```

- `response.read()` tüm ses gelene kadar bloklar; `response.iter_bytes()` ile streaming PCM al, ilk birkaç yüz ms geldiğinde playback kuyruğuna parça parça koy → algılanan gecikme daha da azalır.

## 6. HTTP bağlantı katmanı

Her `OpenAI(...)` instance'ı kendi HTTP client'ını kuruyor; ama `sr`, `llm`, `tts` her biri ayrı OpenAI client. 

- **HTTP/2** + connection pooling (openai SDK httpx tabanlı; `http_client=httpx.Client(http2=True, limits=...)` geçerek handshake maliyetini düşürün.
- `transcriptions.create` şu an **multipart upload** ile tüm WAV'ı gönderiyor; gerçek zamanlı için **Realtime API** veya gRPC streaming ASR (ör. `faster-whisper` lokal) daha düşük latency verir.
- Uzun sürmesi muhtemel API'lar için `timeout_sec` agresif tutun; retry yok (kod iyi), ama bağlantı "keepalive" için openai SDK'nın default'ları yeterli.

## 7. Memory ve GC baskısı

Audio callback her tick'te:
- `np.zeros(frames, ...)` (playback buffer)
- `np.ascontiguousarray(...copy())`
- `cleaned.astype(np.int16).tobytes()`

gibi **çok sayıda kısa ömürlü array** yaratıyor. Gerçek zamanlı thread'de bu GC tetikleyebilir. Pre‑allocated bufferlar (bir `np.empty` havuzu) ile tamamen kaldırılabilir. `gc.disable()` + manuel `gc.collect()` audio streaming servislerinde yaygın bir pattern — ancak dikkatli uygulanmalı.

Ayrıca `InMemoryHistory.add` her sınır aşımında **yeni liste** oluşturuyor:

```46:49:src/ar_voice_controller/providers/llm.py
self._messages.append(message)
if len(self._messages) > self.max_messages:
    self._messages = self._messages[-self.max_messages :]
```

`collections.deque(maxlen=...)` O(1) olur; `snapshot()` da `list(self._messages)` kalabilir.

## 8. Thread-per-subscription modeli

`InProcessBus` her abone için **ayrı thread + ayrı queue** oluşturuyor (`_Subscription`). 15–20 event tipi × birkaç dinleyici = pipeline start'ta 5–10 thread. Python GIL altında context switch maliyeti artar. Alternatif: tek dispatcher thread + lightweight per-topic callback çağrısı. Performans etkisi orta; ama özellikle düşük güçlü donanımda (Raspberry Pi vb. AR donanımı) fark edilir.

## 9. Mikro-optimizasyonlar (etki düşük)

- `VadDetector.int2float` içindeki `np.abs(arr).max()` + conditional scaling — eğer peak sıfırdan farklı ise her defasında full array scan. Sabit bir ölçek (`arr * (1/32768.0)`) yeterli:

```42:48:src/ar_voice_controller/audio/vad.py
arr = np.frombuffer(sound, np.int16).astype("float32")
peak = np.abs(arr).max() if len(arr) > 0 else 0
if peak > 0:
    arr *= 1.0 / 32768.0
```
- `encode_event` her çağrıda `is_dataclass` + `asdict` — cache edilmiş encoder (type→fn) mantığı önemli miktarda hızlandırır.
- `TurnManager.run` ana döngüsü `read_chunk(timeout=0.2)` ile pek çok wakeup yapıyor; 0.2 s çok değil ama condition-based wake (audio thread push + event) daha temiz.
- `deque` yerine list kullanılan yerler zaten az; log mesajlarında `print(..., flush=True)` audio callback içinde — I/O bloke edebilir; logging queue veya rate limit önerilir (satır 102 `_callback`).
- `__slots__` + `@dataclass(slots=True)` zaten kullanılmış, güzel.
- `Path(...).read_text()` her client init'te sistem prompt'u okuyor; küçük dosya, sorun değil.

## 10. Profil çıkar — her şeyden önce bunu yap

Yukarıdaki liste tecrübeye dayalı; gerçek kazanç dağılımını görmek için:

- **End‑to‑end latency breakdown**: ASR başlangıç → final, LLM ilk token → final, TTS ilk byte → playback. `TurnMetrics` event'i zaten var, tüm ara zamanları (sr_latency, ttft, tts_first_audio_ms) ölçmek için bus publish'leri ekleyin.
- **py-spy** veya **scalene** ile canlı pipeline'ı profilleyin; özellikle audio callback thread'inin zamanı kritik.
- `perf` / `flamegraph` ile Python + C extension (aec_audio_processing, torch) birleşik görüntü alın.

Profil sonucu çoğu projede şunu gösterir: **zamanın %90'ı ağ I/O'sunda** (ASR + LLM + TTS). Yani 1, 5 ve 6. maddelerdeki optimizasyonlar hissedilen performansta #2–#4'ten daha büyük fark yaratır. CPU‑bound darboğaz görünüyorsa sıralama 2 → 3 → 4 olur.

---

**Özet öncelik sırası:**

1. İlk TTS segmenti için eşikleri düşür + speculative filler → UX'te en büyük "hızlandı" hissi
2. Streaming ASR / Realtime API → ASR + LLM arası beklemeyi yok eder
3. VAD çağrılarını tekilleştir, ONNX'e geçir, frame boyutunu hizala
4. AEC / audio callback içindeki allocation ve tobytes/frombuffer turunu temizle
5. TTS sentezini paralelleştir + PCM'i stream et + hızlı resampler
6. HTTP/2 + persistent connection + tek `httpx.Client`
7. Event bus için orjson/msgspec; yüksek frekanslı topic'leri batch'le
8. Thread-per-subscription modelini tek dispatcher'a indir
9. Memory/GC hijyeni (pre‑alloc buffers, deque history)
10. Mikro‑optimizasyonlar (int2float sabit ölçek, encoder cache, log rate limit)

Bu öncelik sırası "ortalama kullanıcı gecikmesini" hedefler. CPU/güç kısıtı ön plandaysa (AR cihaz), 2 ve 3 birinciye taşınabilir.
