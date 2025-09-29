---

marp: true
theme: default
title: AI Destekli Kod Yazma Rehberi
class:
  - lead 
paginate: true
style: |
  section {
    font-size: 22px;
    padding-top: 85px;
  }
  section h3 {
    position: fixed;
    top: 10px;
    left: 30px;
    width: 100%;
    padding: 10px 0;
    z-index: 1;
  }
  header {
    z-index: 2;
    width: 95%;
    text-align: right;
  }

---

<!-- _paginate: false -->

# AI Destekli Kod Yazma Rehberi

---

<!-- footer: 30.09.2025 -->
<!-- header: AI Destekli Kod Yazma Rehberi  -->

<style scoped>
section {
    font-size: 18px;
}
ul > li {
    font-weight: bold;
}
</style>

### İçerik

**Sunum:** ~20 dk
**Soru-Cevap:** ~5 dk 

- 💡 Vizyonunu Net Belirle
- 🎨 Önce Planla
- 💾 Git & GitHub'ı İyi Kullan
- 🛠️ Popüler Bir Tech Stack Seç
- 🧩 Karmaşık Özellikleri Parçalara Ayır
- 💬 Chat Context'i Akıllıca Yönet
- ✨ Promptları Düzeltmekten Çekinme
- 🛠️ Kodları AI ile Adım Adım Gözden Geçir
- 🐛 Hataları Etkili Bir Şekilde Yönet
- 📘 "Common AI Mistakes" Dosyası Tut
- 📜 Cursor Rules'u Kullan

*Bu rehber, AI ile daha verimli ve hatasız kodlama yapabilmeniz için temel ipuçlarını ve en iyi uygulamaları adım adım sunmaktadır. \
Buradaki tavsiyelerle hem planlama hem geliştirme süreçlerinizi kolaylaştırabilirsiniz.*

<blockquote>Kaynak: <a href="https://www.reddit.com/r/ClaudeAI/comments/1kivv0w/the_ultimate_vibe_coding_guide/">The Ultimate Vibe Coding Guide</a> by <a href="https://www.reddit.com/user/PhraseProfessional54/">u/PhraseProfessional54</a> in<a href="https://www.reddit.com/r/ClaudeAI/"> ClaudeAI</a></blockquote>

---

### 💡 Vizyonunu Net Belirle

* **Güçlü ve detaylı bir vizyon** ile başla.
* Girdi **belirsiz veya dağınık olmamalı**, aksi halde çıktı da öyle olur.
* **Detaylı ve net promptlar ver**, AI'ın kendi başına karar vermesine izin verme.
* **Plan ne kadar netse**, uygulama o kadar kolay olur.
* **Hem kullanıcı hem de geliştirici** bakış açısıyla düşün.
* **Düşüncelerini yapılandırmak ve detayalandırmak** diğer AI araçlarını kullan.
* Promptlarını detaylandırmak için **başka AI'ları kullanabilirsin.**
* Örneğin;
  * Yapmak istediklerini öncelikle **Claude AI**'ye yazıp, ondan detaylı bir prompt yazmasını iste. 
  * Ardından bu promptu Copilot'a verip çalıştır. 

---

### 🎨 Önce Planla

* **Öncelikle planla**, doğrudan kodlamaya başlama.
* Örneği UI/UX için [**v0**](https://v0.app/) gibi araçlarla tasarımını erken aşamada görselleştirebilirsin.
* **Tutarlılık çok önemli**, baştan bir **tasarım sistemi** seç ve sadık kal.
* **Tekrar kullanılabilir bileşenler** (butonlar, loading indicator, vs.) oluştur.
* **[21st.dev](https://21st.dev/)** kullanarak hazır bileşenler ve AI promptları kopyalayabilirsin.

---

### 💾 Git & GitHub'ı İyi Kullan

* **Git senin en iyi dostun**.
* **AI yanlış kod ürettiğinde**, kolayca eski versiyona dönebilirsin.
* ****Düzenli** olarak commit yapmayı unutma**, özellikle büyük değişiklikler yaparken.
* Bu alışkanlık seni birçok **felaketten kurtarır**.

---

### 🛠️ Popüler Bir Tech Stack Seç

* **Yaygın ve iyi dokümante edilmiş** teknolojilere bağlı kal.
* AI modelleri **en yaygın teknolojilerde daha iyi performans gösterir**.
* **Daha yaygın stack = daha kaliteli kod desteği**.
* Örnek bir stack:
  * **Next.js** → frontend & API
  * **Supabase** → veritabanı & kimlik doğrulama
  * **Tailwind CSS** → stil
  * **Vercel** → hosting
* veya [*FARM Stack*](https://www.mongodb.com/resources/basics/farm-stack):
  * **FastAPI** → backend
  * **React** → frontend
  * **MongoDB** → veritabanı
  * **Heroku** → hosting
* Bilinen bir stack ile ilerlemek **hızlı bir başlangıç yapmanı sağlar ve fazla ayarlama gerektirmez.**

---

### 🧩 Karmaşık Özellikleri Parçalara Ayır

* *"X özelliğini ekle"* gibi **büyük değişiklikleri tek seferde yapma**.
* AI'dan **büyük değişiklikleri tek seferde yapmasını istemek yanlış sonuç üretebilir**.
* Bunun yerine eklenecek özelliği **fazlara böl**.
* Ekleyeceğin özellik karmaşıksa, **öncelikle AI'dan plan yapmasını isteyebilirsin.**
* Ardından plandaki adımları teker teker gerçekleştirmesini iste ve **her bir adımda değişiklikleri gözden geçir.**
* Küçük adımlar → **daha doğru ve kontrol edilebilir sonuçlar**.

---

### 💬 Chat Context'i Akıllıca Yönet

* **Doğru context sağlamak en önemli şeydir**, özellikle büyük kod tabanlarında.
* Değişiklik yapılacak **dosyaları net şekilde belirt**.
* AI'nın **bağlam penceresi (context window) sınırlı**, uzun chat'lerde önceki bilgileri unutabilir.
* Çok uzun context AI'yı **bunaltabilir**, dikkatli ol.
* **Chat çok uzadığında yeni chat bir penceresi aç**.
* **Yeni pencere açınca**, AI'ya üzerinde çalıştığın **özelliği ve dosyaları kısaca özetle**.
* **Doğru context** → daha doğru ve tutarlı sonuçlar.
* **İlgili bileşenleri belirtmek** → AI'nın ihtiyacı olan bilgiyi almasını sağlar.

---

### ✨ Promptları Düzeltmekten Çekinme

* AI yanlış veya istemediğin eklemeler yaptığında, **yaptığı yanlışları belirterek yeniden denemesi iste**.
* **Promptu değiştir ve tekrar gönder**, hatalı kodla devam etme.
* Eğer hataları görmezden gelirsen; AI aynı hataları **tekrar etmeye eğilim gösterir**, bu da yeni hatalara yol açabilir.
* Daha önce oluşturulan **benzer kod parçalarını örnek göster** ve yeni bileşenlerde **aynı tasarım ve davranışı** uygulamasını iste. 
* AI **mevcut desenleri hızlıca öğrenir**.
* **Düzeltme & yeniden deneme** → daha doğru ve temiz sonuçlar.

---

### 🛠️ Kodları AI ile Adım Adım Gözden Geçir

* Değişiklikleri tamamladıktan sonra **ilgili değişiklikeri AI'ya göster ve gözden geçirmesini iste**.
* **Varsa kötü kodlama patternlerini** bulmasını ve nasıl düzeltileceğini yazmasını iste.
* Verdiği önerileri başka bir **AI'ya ver ve düzeltmesini iste.**
* Yani;
  * **Birinci AI**'a review yaptır,
  * **İkinci AI**'a review'in uygulamasını yaptır,
  * **Üçüncü AI**'a hem review'i hem uygulamanın sonucunu verip, nihai bir değerlendirme yapmasını iste.
  * Farklı AI'ları bu şekilde **birbiriyle rekabet içinde kullanarak daha iyi sonuçlar elde edilebilir**.  
* Bu yöntem **performans ve güvenlik sorunlarını erken yakalar**.

---

### 🐛 Hataları Etkili Bir Şekilde Yönet

* Bir hata aldığında **geri dön ve AI'ya isteğini tekrar yaptır**.
* **Hata mesajını AI'ya göster** ve çözmesini sağla.
* **Çok fazla denemeden sonra çözülmezse**, başka bir AI'da aynı prompt ile tekrar dene.
* AI'dan **hatanın geldiği bileşenleri incelemesini ve olası sebepleri listelemesini** iste.
* **Log eklemesini ve çıktıları tekrar vermesini** sağla.
* Yine çözülmezse promptu **düzelt ve doğru context ile tekrar dene**.
* AI bazen **fazladan ekleme, silme veya değiştirme** yapar.
* Değişiklikleri yapmasını isterken buna benzer **net bir cümle ekle**: *"Do not change anything I did not ask for; just do what I told you."*

---

### 📘 "Common AI Mistakes" Dosyası Tut

* AI'n sık yaptığı **hataları bir metin dosyasına kaydet**.
* Yeni bir özellik eklerken **bu dosyayı referans ver**.
* Bu sayede **tekrarlayan hataları önler ve zaman kazanırsın**.
* Bu yöntem, **özellikle büyük değişiklikler yaparken AI'n doğru yönlendirilmesini sağlar** .

---

### 📜 Cursor Rules'u Kullan

* [**Cursor Rules**](https://cursor.com/tr/docs/context/rules), güçlü bir başlangıç sağlar.
* **Tech stack'in ile uyumlu kurallar** oluştur.
* AI modeli için **talimatlar, en iyi uygulamalar ve kaçınılması gerekenler** belirle.
* Hazır şablonlar için [**cursor.directory**](https://cursor.directory/rules) kullanabilirsin.

---

Teşekkürler!
