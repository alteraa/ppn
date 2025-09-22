gpt:


### 📘 Dökümantasyon

* **README.md** → Projenin yüzü; proje hakkında temel bilgiler, kurulum talimatları, kullanım örnekleri ve temel özelliklerin özetini içerir. Genellikle Markdown formatında yazılır ve GitHub/GitLab gibi platformlarda otomatik olarak görüntülenir.

* **CONTRIBUTING.md** → Projeye katkıda bulunmak isteyen geliştiriciler için rehberdir. Kod stil kuralları, branch yönetimi, pull request veya merge request prosedürleri burada belirtilir.

* **CODE\_OF\_CONDUCT.md** → Projeye katılanların uyması beklenen davranış kurallarını belirler. Topluluk yönetimi ve olası anlaşmazlıkların önüne geçmek için kullanılır. Yaygın olarak [Contributor Covenant](https://www.contributor-covenant.org/) kullanılır.

* **SECURITY.md** → Projede güvenlik açıkları veya hataları tespit edenlerin bildirimde bulunması için prosedürleri açıklar. Ayrıca güvenlik politikaları ve raporlama yollarını belirtir.

* **CHANGELOG.md** → Projenin sürümleri arasındaki değişiklikleri kaydeder. Yeni özellikler, düzeltmeler, hata giderimleri gibi bilgileri içerir. Yaygın formatlardan biri [Keep a Changelog](https://keepachangelog.com/) standardıdır.

* **LICENSE** → Projenin lisans bilgisini içerir; kullanıcıların projeyi kullanma, değiştirme veya dağıtma haklarını belirler. Örnek olarak MIT, Apache 2.0 veya GPL lisansları sık kullanılır.

* **docs/** → Daha detaylı, kapsamlı proje dökümantasyonunun saklandığı klasördür. Sphinx veya MkDocs gibi araçlarla HTML, PDF veya başka formatlarda üretilmiş dökümantasyon burada tutulur.


---

claude:

# 📘 Dökümantasyon Kategorisi

## **README.md**
Projenin ana tanıtım dosyası. Kullanıcıların ve geliştiricilerin ilk karşılaştığı dosya. Projenin ne yaptığı, nasıl kurulacağı, nasıl kullanılacağı ve temel örnekleri içerir. GitHub ve diğer git platformlarında otomatik olarak görüntülenir.

**Tipik içerik:** Proje başlığı, açıklama, kurulum talimatları, kullanım örnekleri, katkıda bulunma rehberi linki.

## **CONTRIBUTING.md**
Projeye katkıda bulunmak isteyen geliştiriciler için rehber dosyası. Kod standartları, pull request süreci, issue açma kuralları, geliştirme ortamı kurulumu gibi bilgileri içerir.

**Tipik içerik:** Development setup, coding standards, commit message formatı, testing gereksinimleri, review süreci.

## **CODE_OF_CONDUCT.md**
Proje topluluğu için davranış kurallarını belirleyen dosya. Kabul edilebilir ve edilemez davranışları tanımlar. Özellikle açık kaynak projelerde topluluk yönetimi için kritik.

**Yaygın standart:** Contributor Covenant Code of Conduct en çok kullanılan şablondur.

## **SECURITY.md**
Güvenlik açığı raporlama süreci ve güvenlik politikalarını açıklayan dosya. Güvenlik açığı bulan kişilerin nasıl rapor edeceğini, hangi kanalla iletişim kuracağını belirtir.

**Tipik içerik:** Güvenlik açığı raporlama e-postası, PGP key, responsible disclosure politikası, desteklenen sürümler.

## **CHANGELOG.md**
Projenin sürüm geçmişini ve her sürümde yapılan değişiklikleri kayıt altına alan dosya. Kullanıcıların yeni özellikler, bug fix'ler ve breaking change'leri takip etmesini sağlar.

**Format standardı:** Keep a Changelog formatı yaygın olarak kullanılır. Semantic Versioning ile uyumlu çalışır.

## **LICENSE**
Projenin lisans bilgilerini içeren dosya. Projenin nasıl kullanılabileceğini, dağıtılabileceğini ve değiştirilebileceğini hukuki olarak belirler.

**Yaygın lisanslar:** MIT, Apache 2.0, GPL-3.0, BSD-3-Clause. GitHub lisans seçimi için otomatik şablonlar sunar.

## **docs/**
Detaylı dökümantasyon dosyalarının bulunduğu klasör. API referansları, tutorial'lar, architecture dökümanları gibi kapsamlı dökümantasyon materyalleri içerir.

**Yaygın araçlar:** 
- **Sphinx:** Python projelerinde en çok kullanılan döküman üretici
- **MkDocs:** Markdown tabanlı, basit döküman sitesi oluşturucu
- **GitBook:** Modern, interaktif döküman platformu
- **Read the Docs:** Ücretsiz döküman hosting servisi