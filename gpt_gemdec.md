🧠 Speculative Decoding — Baştan Sona Anlatım

1. Problem: LLM’ler neden yavaş?

Bütün modern LLM’ler autoregressive decoding kullanır:

👉 Token → hesapla → ekle → tekrar et

Yani:

"Hello" → "Hello world" → "Hello world how" → ...

Her token için:

full forward pass gerekir

önceki token bitmeden yenisi başlayamaz


📌 Bu yüzden:

Latency lineer artar

GPU tam kapasite kullanılamaz 



---

2. Core fikir: “Tahmin et, sonra kontrol et”

Speculative decoding’in ana fikri:

> “Büyük model yavaş → küçük model önden tahmin etsin”



Yani iki model var:

Model	Rol

Draft model	Hızlı tahmin eder
Target model	Doğruyu kontrol eder



---

3. Nasıl çalışır? (Adım adım)

🔁 Loop

1. Küçük model K token üretir


2. Büyük model bunları tek seferde kontrol eder


3. Uyuşanları kabul eder


4. Uyuşmayan noktadan devam eder






---

🔍 Görsel Diyagram

Input: "The cat"

Draft model → predicts:
[ sat | on | the | mat ]

Target model (single pass):
✔ sat
✔ on
✔ the
✖ mat (reject)

Final output:
"The cat sat on the"


---

4. Neden hızlı?

Normalde:

5 token → 5 forward pass

Speculative:

5 token → 1 forward pass

💥 Çünkü:

GPU memory-bound (hesap değil veri taşıma bottleneck) 

Aynı anda birden fazla token kontrol etmek “bedava” gibi



---

5. Kalite neden bozulmaz?

Çok kritik nokta 👇

👉 Final output = target model output

Çünkü:

Sadece target model onayladıklarını alıyoruz

rejection sampling kullanılıyor 



---

6. Performans metrikleri

📊 Acceptance Rate (α)

Draft token’ların kabul edilme oranı

En kritik metrik


📊 Speculative Length (γ)

Kaç token ileri tahmin ediliyor


📊 Accepted Tokens (τ)

Ortalama kabul edilen token sayısı



---

7. Ne zaman işe yarar?

✅ İyi durumlar:

Chatbot

Code completion

Low-latency sistemler


❌ Kötü durumlar:

Draft model kötü ise

Acceptance düşükse

GPU memory limitliyse



---

8. Varyantlar (ileri seviye ama sunumda mention edilebilir)

SpecInfer → tree-based decoding

Medusa → ekstra head’ler

EAGLE → hidden representation üzerinden 



---

9. Özet

👉 Problem: Sequential decoding
👉 Çözüm: Parallel verification
👉 Sonuç: 2–3x hızlanma


---

🎤 Şimdi: Marp Sunum (Markdown)

Aşağıdaki direkt kullanılabilir 👇


---

---
marp: true
theme: default
paginate: true
---

# Speculative Decoding
## Faster LLM Inference

---

# Problem: Why are LLMs slow?

- Autoregressive generation
- One token at a time
- Sequential dependency


Token → Forward Pass → Next Token


⛔ Cannot parallelize

---

# Bottleneck

- Each token = full model pass
- GPU mostly waiting on memory

👉 High latency

---

# Key Idea

## "Guess ahead, then verify"

Use two models:

- 🟢 Draft Model (fast)
- 🔵 Target Model (accurate)

---

# High-Level Flow

1. Draft model predicts multiple tokens
2. Target model verifies in parallel
3. Accept correct tokens
4. Repeat

---

# Diagram


Input: "The cat"

Draft:
[ sat | on | the | mat ]

Target:
✔ sat
✔ on
✔ the
✖ mat

Output:
"The cat sat on the"


---

# Normal vs Speculative

## Normal

- 5 tokens → 5 passes

## Speculative

- 5 tokens → 1 pass

🚀 Speedup: 2–3x

---

# Why It Works

- LLM inference is memory-bound
- GPU compute is underused
- Parallel verification is cheap

---

# Quality Guarantee

✔ Output identical to target model

Because:
- Only accepted tokens are used
- Target model always validates

---

# Key Metrics

- **Acceptance Rate (α)**
- **Speculative Length (γ)**
- **Accepted Tokens (τ)**

---

# Performance Insight

- High α → high speedup
- Low α → wasted computation

---

# When to Use?

✅ Chatbots  
✅ Code completion  
✅ Real-time systems  

❌ Weak draft model  
❌ Low acceptance rate  

---

# Variants

- SpecInfer (tree-based)
- Medusa (multi-head)
- EAGLE (feature-level)

---

# Summary

- Problem: Sequential decoding
- Solution: Draft + Verify
- Result: Faster inference without quality loss

---

# Thank You 🚀
