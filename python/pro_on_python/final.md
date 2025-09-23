### 📘 Dökümantasyon

- README.md
  - Projenin ana tanıtım dosyası.
  - Kullanıcıların ve geliştiricilerin ilk karşılaştığı dosya.
  - Projenin ne yaptığı, nasıl kurulacağı, nasıl kullanılacağı ve temel örnekleri içerir.
  - İçerik: Proje başlığı, açıklama, kurulum talimatları, kullanım örnekleri, katkıda bulunma rehberi linki.
- CONTRIBUTING.md
  - Projeye katkıda bulunmak isteyen geliştiriciler için rehber dosyası. 
  - Kod standartları, pull request süreci, issue açma kuralları, geliştirme ortamı kurulumu gibi bilgileri içerir.
  - İçerik: Development setup, coding standards, commit message formatı, testing gereksinimleri, review süreci.
- CODE_OF_CONDUCT.md
  - Projeye katılanların uyması beklenen davranış kurallarını belirler. 
  - Topluluk yönetimi ve olası anlaşmazlıkların önüne geçmek için kullanılır. 
  - Yaygın olarak [Contributor Covenant](https://www.contributor-covenant.org/) kullanılır.
- SECURITY.md
  - Güvenlik açığı raporlama süreci ve güvenlik politikalarını açıklayan dosya.
  - Güvenlik açığı bulan kişilerin nasıl rapor edeceğini, hangi kanalla iletişim kuracağını belirtir.
  - İçerik: Güvenlik açığı raporlama e-postası, PGP key, responsible disclosure politikası, desteklenen sürümler
- CHANGELOG.md
  - Projenin sürüm geçmişini ve her sürümde yapılan değişiklikleri kayıt altına alan dosya. 
  - Kullanıcıların yeni özellikler, bug fix'ler ve breaking change'leri takip etmesini sağlar.
  - Yaygın formatlardan biri [Keep a Changelog](https://keepachangelog.com/) standardıdır.
- LICENSE
  - Projenin lisans bilgilerini içeren dosya. 
  - Projenin nasıl kullanılabileceğini, dağıtılabileceğini ve değiştirilebileceğini hukuki olarak belirler.
  - Örnek olarak MIT, Apache 2.0 veya GPL lisansları sık kullanılır.
- docs/
  - Daha detaylı, kapsamlı proje dökümantasyonunun saklandığı klasördür.
    - Sphinx: Python projelerinde en çok kullanılan döküman üretici
    - MkDocs: Markdown tabanlı, basit döküman sitesi oluşturucu
    - GitBook: Modern, interaktif döküman platformu
    - Read the Docs: Ücretsiz döküman hosting servisi

### 📦 Paketleme & Dağıtım

- setup.py
  - Python paketlerinin klasik yapılandırma dosyasıdır. Paket adı, sürüm, yazar bilgisi, bağımlılıklar ve `entry_points` gibi bilgiler burada tanımlanır. 
  - `setuptools` veya `distutils` ile paketleme ve dağıtım yapılır.
- pyproject.toml
  - Modern Python projelerinde yapılandırma ve paketleme için kullanılan dosyadır. 
  - `PEP 518` standardına uygundur ve `build-backend` ile hangi araçla paketleme yapılacağını belirtir. 
  - Tüm proje ayarlarını tek bir dosyada toplar: build system, dependencies, tool konfigürasyonları.
- setup.cfg
  - `setup.py` yerine veya yanında, yapılandırma bilgilerini statik olarak tutmak için kullanılır. 
  - Paket metadata, test komutları ve entry-point tanımlamaları gibi bilgiler içerir.
- requirements.txt
  - Projenin çalışması için gereken bağımlılıkları listeler. 
  - `pip install -r requirements.txt` ile kolayca yüklenebilir.
- requirements-dev.txt
  - Development ve testing için gerekli olan ek bağımlılıkları içerir. 
  - Production'da gerekmeyen araçlar: linting, testing, documentation tools.
- Pipfile / Pipfile.lock
  - Pipenv aracı tarafından kullanılan dosyalardır. 
  - `Pipfile` bağımlılıkları tanımlar, `Pipfile.lock` ise sürümleri sabitleyerek tekrar üretilebilir ortam sağlar.
- poetry.lock
  - Poetry paket yönetiminde bağımlılıkların sabitlenmesini sağlar. 
  - `pyproject.toml` ile birlikte kullanılır ve projenin bağımlılıklarını tam olarak kontrol etmeye yarar.
  - Tüm bağımlılıkların tam sürümlerini ve hash'lerini içerir, reproducible builds sağlar.
- MANIFEST.in
  - Kaynak dağıtımına (sdist) hangi ek dosyaların (doküman, veri dosyası, script vb.) pakete dahil edileceğini belirtir.
  - setup.py build işleminde kullanılır.
- py.typed
  - Paketinizin type hints içerdiğini ve type checker'lar tarafından kontrol edilebileceğini belirten işaretleyici dosya (PEP 561).
  - mypy, PyCharm gibi type checker'ların paketinizi type-safe olarak tanıması ve PyPI'da yayınlanan kütüphaneler için önemlidir.

### ⚙️ Otomasyon & İş Akışı

- Makefile
  - Unix/Linux ortamlarında yaygın olarak kullanılan görev otomasyon dosyasıdır. 
  - Test, lint, build veya run gibi sık yapılan komutları tek bir komutla çalıştırmayı sağlar.
- justfile
  -  Makefile’a modern ve daha okunabilir bir alternatiftir.
  -  `just` aracı ile kullanılır; görevler basit sözdizimiyle tanımlanır ve bağımlılık yönetimi, task chaining gibi özellikler sunar.
- invoke.yaml / tasks.py
  - Python tabanlı görev otomasyon sistemidir. 
  - `invoke` aracıyla, Python kodu ile görevler (tasks) tanımlanabilir ve CLI üzerinden çalıştırılabilir.
- tox.ini
  - **Tox** test automation aracının konfigürasyon dosyası.
  - Farklı Python sürümleri ve environments'da otomatik testing yapar.
- noxfile.py
  - Tox’un modern alternatifi olarak görülebilir.
  - Python ile yazılır ve test, lint, format gibi görevleri esnek bir şekilde tanımlamayı sağlar.
- CMakeLists.txt
  - Python projelerinde özellikle C/C++ ile yazılmış native extension veya bağımlılıkların derlenmesi için kullanılan build yapılandırma dosyasıdır. 
  - Çok platformlu derleme ve bağımlılık yönetimi sağlar.

### ✅ Kalite Kontrol & Stil

- .flake8
  - Python kodunu PEP8 standartlarına göre kontrol eden `flake8` aracının ayar dosyasıdır. 
  - Hangi uyarıların görüneceği veya hangi dosyaların hariç tutulacağı burada belirlenir.
  - Şunları kontrol eder: Code style, logical errors, cyclomatic complexity, naming conventions, docstring presence.
- .pylintrc
  - `pylint` aracı için yapılandırma dosyasıdır.
  - Kod kalitesi, stil ve hata tespiti ile ilgili kurallar burada tanımlanır.
- .editorconfig
  - Farklı editör ve IDE’lerde ortak kod stili sağlamak için kullanılır. 
  - Satır uzunluğu, boşluk karakterleri, dosya sonu boşlukları gibi ayarlar içerir.
- .pre-commit-config.yaml
  -  Git commit’leri öncesinde otomatik olarak kod formatlama, lint veya güvenlik kontrolleri yapan pre-commit hook’larını tanımlar.
- .isort.cfg
   - Python importlarını alfabetik ve mantıksal sıraya göre düzenleyen `isort` aracının ayarlarıdır.
- .black.toml
  - Python kodunu standart bir formatta biçimlendiren `black` aracının ayarlarıdır. 
  - Kod stilini otomatik olarak uygular.
- .bandit / .bandit.yml
  - Python kodunu güvenlik açıkları açısından tarayan `bandit` aracının ayar dosyasıdır. 
  - Riskli kod desenlerini tespit eder.
- mypy.ini
  - Python’da tip denetimi yapan `mypy` aracının yapılandırmasıdır. 
  - Hangi dosyaların kontrol edileceği ve hangi kuralların uygulanacağı burada tanımlanır.
- pyrightconfig.json
  - Microsoft’un geliştirdiği `Pyright` tipi denetleyici aracının yapılandırma dosyasıdır. 
  - Projeye yönelik tip kontrol ayarlarını JSON formatında belirtir.


### 🔒 Güvenlik & Analiz

- safety-policy.json
  - Projedeki güvenlik açıklarının raporlanması ve yönetilmesi için kullanılan bir yapılandırma dosyasıdır. 
  - `safety` aracı ile Python paketlerinin bilinen güvenlik açıklarını taramak ve politika kurallarını uygulamak için kullanılır.
- .snyk
  - `Snyk` güvenlik platformu tarafından kullanılan konfigürasyon dosyasıdır. Projenin bağımlılıklarını analiz ederek güvenlik açıklarını bulur ve raporlar. 
  - Ayrıca, hangi açıkların ignore edileceği veya hangi policy’nin geçerli olacağı gibi bilgileri içerir.




### 🧪 Test & Örnekler

- tests/
  - Projenin birim testleri ve entegrasyon testlerinin saklandığı ana klasördür. 
  - Genellikle `pytest` veya `unittest` ile yazılmış test dosyaları içerir.
  - Test dosyaları `test_` prefix'i veya `_test` suffix'i kullanır.
- conftest.py
  - `pytest` ile ortak fixture ve hook’ların tanımlandığı dosyadır. 
  - Testler arasında paylaşılan setup/teardown işlemleri burada yapılır.
- pytest.ini
  - `pytest` test framework’ünün yapılandırma dosyasıdır. 
  - Test discovery, marker tanımları ve test parametreleri burada belirlenir.
- coverage.rc
  - Kod kapsama (coverage) araçları için yapılandırma dosyasıdır. 
  - Hangi dosyaların ölçüleceği, hangi dosyaların hariç tutulacağı gibi ayarlar içerir.
- .hypothesis/
  - `Hypothesis` kütüphanesi ile property-based testing yapılırken oluşturulan cache ve ayar klasörüdür. 
  - Testlerin deterministik ve tekrar edilebilir olmasını sağlar.
- examples/
  - Projenin kullanımını gösteren örnek kodlar veya scriptlerin bulunduğu klasördür. 
  - Kullanıcıların ve geliştiricilerin projeyi hızlıca anlamasına yardımcı olur.

### 🚀 CI/CD & Deployment

- .gitignore
  - Git’in takip etmeyeceği dosya ve klasörleri belirtir. 
  - Örneğin cache, derleme çıktıları ve IDE konfigürasyonları burada listelenir.
  - Python-specific: `__pycache__/`, `*.pyc`, `.env`, `venv/`, `dist/`, `.coverage`, `.pytest_cache/`
  - IDE/Editor: `.vscode/`, `.idea/`, `*.swp`, `.DS_Store`
- .gitattributes
  - Git için dosya türleri ve satır sonu gibi ayarları tanımlar. 
  - Farklı platformlarda tutarlılık sağlar.
- .github/workflows/
  - CI/CD pipeline'larının tanımlandığı klasör.
  - Test, build ve deploy işlemleri burada otomatikleştirilir.
- .gitlab-ci.yml
  - GitLab CI/CD pipeline’ını tanımlayan dosyadır. 
  - İş akışları, stage’ler ve job’lar burada yapılandırılır.
- Jenkinsfile
  - Jenkins ile pipeline’ların kod olarak tanımlandığı dosyadır. 
  - Test, build, deploy aşamaları burada yönetilir.
- Dockerfile
  - Projeyi container içinde çalıştırmak için gerekli yapılandırmayı içerir. 
  - Ortam bağımlılıkları ve komutlar burada tanımlanır.
- docker-compose.yml
  - Birden fazla container’ın birlikte çalıştırılmasını sağlar. 
  - Servisler, network ve volume ayarları burada tanımlanır.
- k8s/
  - Kubernetes deployment, service, configmap gibi manifest dosyalarının bulunduğu klasördür. 
  - Cloud veya container orkestrasyonu için kullanılır.
- runtime.txt
  - [Heroku](https://www.heroku.com/) ve benzeri PaaS (Platform as a Service) ortamlarında kullanılan, projenin çalışacağı Python sürümünü belirten dosyadır. 
  - Örneğin Heroku üzerinde deploy için kullanılır.

### 🌍 Environment & Config

- .env / .env.example
  - Projenin ortam değişkenlerini saklamak için kullanılır. 
  - API anahtarları, veritabanı bağlantıları veya gizli bilgiler burada tanımlanır. 
  - `.env.example` dosyası, örnek ortam değişkenlerini paylaşmak için kullanılır.
- config.ini / config.yaml
  - Uygulama konfigürasyonlarını (ayarlar, parametreler) tutmak için kullanılan yapılandırma dosyalarıdır. 
  - YAML veya INI formatı, okunabilir ve yönetilebilir olmaları nedeniyle tercih edilir.
- .python-version
  - `pyenv` gibi araçlar için kullanılan dosyadır. 
  - Projenin hangi Python sürümünde çalışacağını belirtir ve ortamın tutarlılığını sağlar.

### 💻 Development & IDE

- .vscode/
  - Visual Studio Code için proje bazlı ayarların, eklenti konfigürasyonlarının ve workspace ayarlarının bulunduğu klasördür. 
  - Launch konfigurasyonları, formatter ve linter ayarları gibi bilgiler burada saklanır.
  - `settings.json`:  Workspace-specific VS Code ayarları, Python interpreter path, formatter settings
  - `extensions.json`: Recommended extensions listesi, team members için automatic suggestions
  - `launch.json`: Debug configurations, breakpoint settings, environment variables
  - `tasks.json`: Custom build/run tasks, terminal commands automation
- .idea/
  - JetBrains IDE’leri (PyCharm, IntelliJ IDEA vb.) için proje ayarlarını, kod stili ve workspace bilgilerini tutan klasördür. 
  - Kod tamamlama, debugger ve proje yapısı gibi ayarları içerir.

### 📊 Data & Assets

- data/
  - Projede kullanılan ham veri veya işlenmiş veri dosyalarının saklandığı klasördür. 
  - Örneğin CSV, JSON veya veritabanı dump’ları burada bulunabilir.
- assets/
  - Görseller, ikonlar, fontlar veya proje tarafından kullanılan medya dosyalarının bulunduğu klasördür. 
  - UI veya dokümantasyon için gerekli olan tüm görsel materyaller burada tutulur.
- locale/
  - Çok dilli (i18n) projelerde çeviri dosyalarının ve yerelleştirme kaynaklarının bulunduğu klasördür. 
  - `.po`, `.mo` veya JSON formatları sık kullanılır.
- stub-packages/
  - Python tip stub dosyalarının (`.pyi`) bulunduğu klasördür. 
  - Tip kontrol araçları (mypy, pyright) için third-party paketlerin tip bilgilerini sağlar.

### 🗑️ Geçici / Otomatik Üretilen Dosyalar

- \*.pyc
  - Python kaynak kodlarının derlenmiş bytecode dosyalarıdır. 
  - Performansı artırmak için Python tarafından otomatik üretilir.
  - Python 3.2+ sonrası `__pycache__/` klasörü içinde organize edilir.
- \*.pyo
  - Optimize edilmiş Python bytecode dosyalarıdır. 
  - `python -O` ile çalıştırıldığında oluşturulur.
  - Python 3.5+ için geçerli değildir.
- \*.pyd
  - Windows üzerinde derlenmiş Python extension modüllerini temsil eder (C/C++ ile yazılmış modüller).
  - Linux'taki `.so` (Shared Object) dosyalarının Windows karşılığıdır.
- \*.types
  - Bazı tip kontrol araçları (ör. mypy) tarafından oluşturulan tip anotasyonu dosyalarıdır.
- \*\*pycache\*\*/
  - Python’un bytecode cache klasörüdür. `*.pyc` dosyaları burada tutulur.
- .mypy\_cache/
  - `mypy` tip kontrolü sırasında oluşturulan cache klasörüdür. 
  - Tip kontrolünü hızlandırır.
- .pytest\_cache/
  - `pytest` test framework’ü tarafından oluşturulan geçici cache klasörüdür. 
  - Test sonuçlarının ve konfigurasyonun hızlı erişimi için kullanılır.
- .coverage / htmlcov/
  - Kod coverage araçları tarafından oluşturulan dosya ve rapor klasörleridir. 
  - Test kapsamını gösterir.
- build/
  - Paketleme veya derleme sürecinde geçici olarak üretilen dosyaların tutulduğu klasördür.
- dist/
  - Dağıtılabilir paketlerin (`.tar.gz`, `.whl`) oluşturulduğu klasördür.
- \*.egg-info/
  - Paket metadata ve build bilgilerini tutan klasördür.
  - `setuptools` ile paketleme sırasında üretilir.


### 🧩 Native Extension / Binding Dosyaları

- \*.c
  - C dilinde yazılmış kaynak kod dosyalarıdır. 
  - Python ile native extension geliştirmek için kullanılır.
- \*.cpp
  - C++ dilinde yazılmış kaynak kod dosyalarıdır. 
  - Performans artırımı veya mevcut C++ kütüphanelerini Python’a bağlamak için kullanılır.
- \*.h
  - C/C++ header dosyalarıdır. 
  - Fonksiyon ve sınıf deklarasyonlarını içerir ve diğer kaynak dosyalarında include edilir.
- \*.hpp
  - C++ header dosyalarıdır. 
  - `.h` ile aynı işlevi görür, genellikle C++ projelerinde tercih edilir.
- \*.pyx
  - Cython kaynak kod dosyalarıdır. 
  - Python ile C/C++ kodunu birleştirerek performans artırımı sağlar.
- \*.pxd
  - Cython header dosyalarıdır. 
  - C fonksiyon ve yapılarını `.pyx` dosyalarına tanıtmak için kullanılır.
- \*.pxi
  - Cython include dosyalarıdır. 
  - Ortak kod parçalarını farklı `.pyx` dosyalarında paylaşmak için kullanılır.
- \*.i
  - SWIG interface dosyalarıdır. 
  - C/C++ kodunu Python’a bind etmek için kullanılır; hangi fonksiyonların ve sınıfların Python’a aktarılacağını belirler.
