gpt:


### 📊 Data & Assets

* **data/** → Projede kullanılan ham veri veya işlenmiş veri dosyalarının saklandığı klasördür. Örneğin CSV, JSON veya veritabanı dump’ları burada bulunabilir.

* **assets/** → Görseller, ikonlar, fontlar veya proje tarafından kullanılan medya dosyalarının bulunduğu klasördür. UI veya dokümantasyon için gerekli olan tüm görsel materyaller burada tutulur.

* **locale/** → Çok dilli (i18n) projelerde çeviri dosyalarının ve yerelleştirme kaynaklarının bulunduğu klasördür. `.po`, `.mo` veya JSON formatları sık kullanılır.

* **stub-packages/** → Python tip stub dosyalarının (`.pyi`) bulunduğu klasördür. Tip kontrol araçları (mypy, pyright) için third-party paketlerin tip bilgilerini sağlar.


---

claude:

# 📊 Data & Assets Kategorisi

## **data/**
Projenin kullandığı veri dosyalarının organize edildiği klasör. Raw data, processed data, sample datasets, configuration data gibi çeşitli veri türlerini içerir.

**Tipik alt klasörler:**
- **raw/:** İşlenmemiş, orijinal veri dosyaları (CSV, JSON, XML)
- **processed/:** Temizlenmiş, dönüştürülmüş veriler
- **sample/:** Test ve demo amaçlı küçük veri setleri
- **external/:** Third-party kaynaklardan alınan veriler

**Data science workflows:** 
- **EDA (Exploratory Data Analysis):** Jupyter notebooks ile data exploration
- **ETL pipelines:** Extract, Transform, Load processes için source data
- **Model training:** Machine learning model'leri için training/validation datasets

**Best practices:** Large files için Git LFS kullanımı, sensitive data için .gitignore, versioned data management.

**Format diversity:** CSV, JSON, Parquet, HDF5, SQLite databases, binary formats support.

## **assets/**
Statik dosyalar ve multimedia içeriklerin bulunduğu klasör. Images, stylesheets, JavaScript files, fonts gibi web/UI assets'leri içerir.

**Web applications:**
- **static/:** CSS, JavaScript, images for web interfaces
- **templates/:** HTML template files (Jinja2, Django templates)
- **media/:** User-uploaded content, dynamic media files

**Desktop applications:**
- **icons/:** Application icons, UI element graphics
- **fonts/:** Custom font files, typography assets
- **themes/:** UI theme configurations, color schemes

**Documentation assets:**
- **images/:** README, docs için screenshots, diagrams
- **videos/:** Tutorial videos, demo recordings
- **logos/:** Project branding materials

**Optimization:** Image compression, asset bundling, CDN integration for web deployment.

## **locale/**
Internationalization (i18n) ve localization (l10n) için çoklu dil desteği dosyalarının klasörü. Multilingual applications için language-specific content.

**GNU gettext format:**
- **messages.pot:** Portable Object Template, source strings
- **LC_MESSAGES/:** Language-specific translation files
- **messages.po:** Human-readable translation files  
- **messages.mo:** Binary compiled translation files

**Klasör yapısı:**
```
locale/
├── en/LC_MESSAGES/
├── es/LC_MESSAGES/
├── fr/LC_MESSAGES/
└── tr/LC_MESSAGES/
```

**Python integration:** 
- **babel:** Translation extraction, compilation tools
- **gettext module:** Runtime translation loading
- **Django i18n:** Built-in internationalization framework

**Workflow:** String extraction → Translation → Compilation → Runtime loading

## **stub-packages/**
Type hint stub dosyalarını içeren klasör. Third-party libraries için type information, untyped packages için type stubs.

**Type stub files (.pyi):**
- **Interface definitions:** Function signatures, class definitions without implementation
- **Type annotations:** Static type checker'lar için hint information
- **Protocol definitions:** Structural typing, interface contracts

**Use cases:**
- **Legacy libraries:** Type hints olmayan eski kütüphaneler için type information
- **C extensions:** Native extensions için Python-compatible type definitions  
- **Third-party packages:** Community-contributed type stubs

**Distribution:**
- **typeshed:** Official type stubs repository, mypy tarafından maintain ediliyor
- **@types packages:** npm pattern'den Python'a adaptasyon
- **PEP 561:** Type information distribution standardı

**Integration:** mypy, PyCharm, Pylance gibi type checker'lar otomatik olarak stub files'ı discover eder.

**Development workflow:** `mypy --install-types` ile automatic stub installation, IDE'lerde better code completion.

