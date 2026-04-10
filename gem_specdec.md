d---
marp: true
theme: default
paginate: true
header: "Büyük Dil Modellerinde Hızlandırma: Speculative Decoding"
footer: "Giriş Seviyesi Eğitim Sunumu"
---

# Speculative Decoding: Yapay Zeka Üretimini Hızlandırmak
## Büyük Dil Modelleri (LLM) İçin Modern Çıkarım Optimizasyonu
**Sunum Süresi:** 15-20 Dakika
**Seviye:** Giriş Seviyesi

---

## Geleneksel Dil Modelleri Nasıl Çalışır?

- Büyük Dil Modelleri (LLM'ler) metinleri **sıralı (autoregressive)** olarak üretir.
- Önce bir kelime (token) üretilir. Bu kelime girdi olarak başa döner, sistem tekrar çalışır ve bir sonraki kelime üretilir.
- Tıpkı domino taşları gibidir; 100. kelimeyi üretmek için önceki 99 kelimenin eksiksiz tamamlanması şarttır.
- Bu zorunlu adım adım bağımlılık, sistemin hızını temelden sınırlar.



---

## Neden Yavaşız? (Donanım Darboğazı)

- Güncel grafik işlemcileri (GPU'lar) devasa matematiksel işlem kapasitesine sahiptir.
- Ancak her kelime üretimi için, modelin yüz milyarlarca ağırlık parametresinin hafızadan (VRAM) işlemci çekirdeklerine taşınması gerekir.
- **Hafıza Darboğazı (Memory Bound):** GPU'lar hesaplama yapmaktan çok, hafızadan yeni verinin gelmesini beklerken zaman kaybeder.
- Sadece tek bir kelime üretmek için bütün sistemi bekletmek, o devasa işlem gücünün atıl kalmasına neden olur.



---

## Çözüm Arayışı ve Temel Fikir

- Hızlanmak için daha küçük yapay zeka modelleri kullanırsak sistem hızlanır, ancak bu sefer kalite ve zeka düşer.
- **Hedef:** Büyük modelin yüksek zekasını koruyarak kelime üretim hızını (throughput) artırmak.
- **Çözüm:** *Speculative Decoding (Tahmine Dayalı Kod Çözme)*.
- Bu yöntem, ağır işleri üstlenmesi için büyük modelin yanına daha hızlı çalışan bir "asistan" model ekler ve paralel donanım mimarisinden faydalanır.

---

## Mantık: İki Modelin Birlikteliği

Speculative Decoding, süreci iki farklı modelle yönetir:

1. **Taslak Modeli (Draft Model):** Oldukça küçük, hafif ve milisaniyeler içinde çalışan "asistan" modeldir. Gelecekteki birkaç kelimeyi tahmin ederek taslak oluşturur.
2. **Hedef Model (Target Model):** Asıl kullanmak istediğimiz, devasa ve zeki modeldir (Örn: Llama-3 70B). "Usta" olarak görev yapar ve asistanın ürettiği taslağı kontrol eder.

*Ana Fikir:* "Asistan hızlıca bir taslak hazırlasın, Usta bu taslağı tek seferde kontrol edip onaylasın."



---

## Adım 1: Hızlı Taslak Üretimi (Drafting)

- Kelime üretim süreci, küçük asistan modelin (taslak modelinin) devreye girmesiyle başlar.
- Taslak modeli, asıl büyük modeli beklemeden kendi başına ve çok yüksek hızda peş peşe K adet kelime üretir (örneğin 4 kelime).
- İnsan dilindeki pek çok kelime (bağlaçlar, yaygın tamlamalar, ekler) zaten tahmin edilmesi kolay yapılardır. Küçük model, bu basit kısımları büyük model kadar yüksek doğrulukla ve çok daha ucuza tahmin edebilir.

---

## Adım 2: Tek Seferde Doğrulama (Verification)

Buradaki en büyük sihir doğrulama aşamasındadır:

- Taslak modelinin ürettiği 4 kelime, büyük modele (hedef model) **tek bir paket halinde** gönderilir.
- Büyük model, kelimeleri eskisi gibi tek tek okuyup üretmek yerine, önüne gelen bu dizinin doğru olup olmadığını **tek bir işlemde (paralel olarak)** hesaplar.
- Bu paralel doğrulama mekanizması sayesinde, GPU'nun boşta bekleyen tüm işlem gücü tam kapasiteyle kullanılmış olur.



---

## Adım 3: Kabul veya Reddetme (Accept / Reject)

Büyük model taslağı inceledikten sonra bir ağaç mantığıyla karar verir:

- Eğer taslak kelime, büyük modelin de "evet, ben de bunu üretirdim" diyeceği bir kelimeyse **Kabul Edilir (Accept)**.
- Eğer büyük model o kelimenin yanlış ya da bağlama uygunsuz olduğunu hesaplarsa kelime **Reddedilir (Reject)**.
- Reddedilen kelimeden sonraki tüm taslak kelimeler çöpe atılır ve büyük model o noktada doğru kelimeyi kendisi yazar.



---

## Pratik Bir Örnek Senaryo

**Kullanıcı Girdisi:** "Bugün hava çok..."

- **Asistan Model Hızla Üretir:** "...güzel, yürüyüşe çıkalım mı?" (4 Kelime)
- **Büyük Model Kontrol Eder:**
  - "güzel" -> **Kabul!**
  - "," -> **Kabul!**
  - "yürüyüşe" -> **Ret!** (Büyük modelin zekasına göre bağlam "denize" olmalıydı).
- **Sonuç:** "Bugün hava çok güzel, denize..." olarak çıktı verilir.
- **Kazanç:** Zaman kaybetmeden tek bir adımda 3 doğru kelime ("güzel", ",", "denize") onaylanmış ve üretilmiş oldu.

---

## Çıktı Kalitesi Düşer mi?

- En çok sorulan sorulardan biri: *"Araya küçük model girince yapay zekamın kalitesi veya zekası düşer mi?"*
- **Cevap: Kesinlikle Hayır!**
- Speculative Decoding matematiksel olarak **Kusursuz Örnekleme (Exact Sampling)** garantisi verir.
- Asıl büyük model, uymayan tüm tokenleri reddettiği için nihai çıktı, sanki sistemde asistan model hiç yokmuş ve sadece büyük model çalışmış gibi birebir aynıdır. Sadece hedefe çok daha hızlı varılır.

---

## Performansı Neler Belirler?

Speculative Decoding kurarken iki temel metrik hızlanmayı belirler:

1. **Kabul Oranı (Acceptance Rate - α):** Büyük modelin taslakları ne sıklıkla kabul ettiğidir. İki modelin mimarisi ve kelime dağarcığı ne kadar uyumluysa bu oran o kadar artar.
2. **Taslak Uzunluğu (Speculative Token Count - γ):** Asistanın tek seferde kaç kelime ürettiğidir. Sayı çok yüksek olursa ve usta model hepsini reddederse işlem gücü israf edilir. Sayı çok az olursa sistemin hızlanma potansiyeli kısıtlanır. Genelde 3 ile 5 arası idealdir.

---

## Yeni Nesil Yaklaşımlar (Medusa ve MTP)

- Sistemi iki farklı model (asistan ve usta) olarak kurmak, bilgisayar hafızasında yer sıkıntısına yol açabilir.
- Yeni teknikler (Medusa, Multi-Token Prediction - MTP, EAGLE gibi), ayrı bir küçük asistan model kullanmak yerine **büyük modelin kendisine ekstra tahmin "kafaları" (heads)** ekler.
- Bu sayede model dışarıdan yardıma ihtiyaç duymadan kendi iç yapısıyla gelecekteki tokenleri tahmin eder. Ayrı model yükleme gecikmesi ortadan kalkar.

---

## Özet ve Kazanımlar

- **Zaman Tasarrufu:** Metin üretim hızını, modelin doğruluğunu bozmadan 2 ila 3 kat oranında artırabilir.
- **Donanım Verimliliği:** GPU'lardaki bellek darboğazını (memory bottleneck) aşarak cihazın hesaplama yeteneğini zirveye çıkarır.
- **Kusursuz Kalite:** Taslak-doğrulama mantığı sayesinde, nihai metin kalitesi asıl büyük modelin zekasıyla %100 aynı kalır.
- Büyük yapay zeka modellerinin geleceği, sadece modelleri büyütmekte değil, Speculative Decoding gibi akıllı mühendislik çözümleriyle verimliliği artırmaktan geçmektedir.
