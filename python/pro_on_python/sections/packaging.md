gpt:


### 📦 Paketleme & Dağıtım

* **setup.py** → Python paketlerinin klasik yapılandırma dosyasıdır. Paket adı, sürüm, yazar bilgisi, bağımlılıklar ve `entry_points` gibi bilgiler burada tanımlanır. `setuptools` veya `distutils` ile paketleme ve dağıtım yapılır.

* **pyproject.toml** → Modern Python projelerinde yapılandırma ve paketleme için kullanılan dosyadır. `PEP 518` standardına uygundur ve `build-backend` ile hangi araçla paketleme yapılacağını belirtir. Black, isort gibi araçlar için de ayarları burada tutmak yaygındır.

* **setup.cfg** → `setup.py` yerine veya yanında, yapılandırma bilgilerini statik olarak tutmak için kullanılır. Paket metadata, test komutları ve entry-point tanımlamaları gibi bilgiler içerir.

* **requirements.txt** → Projenin çalışması için gereken bağımlılıkları listeler. `pip install -r requirements.txt` ile kolayca yüklenebilir.

* **requirements-dev.txt** → Geliştirme ve test sürecinde kullanılan bağımlılıkları içerir. Örneğin `pytest`, `mypy` veya `black` gibi araçlar burada tanımlanır.

* **Pipfile / Pipfile.lock** → Pipenv aracı tarafından kullanılan dosyalardır. `Pipfile` bağımlılıkları tanımlar, `Pipfile.lock` ise sürümleri sabitleyerek tekrar üretilebilir ortam sağlar.

* **poetry.lock** → Poetry paket yönetiminde bağımlılıkların sabitlenmesini sağlar. `pyproject.toml` ile birlikte kullanılır ve projenin bağımlılıklarını tam olarak kontrol etmeye yarar.

* **MANIFEST.in** → Kaynak dağıtımı sırasında hangi ek dosyaların (doküman, veri dosyası, script vb.) pakete dahil edileceğini belirtir.

* **py.typed** → Projede tip anotasyonlarının bulunduğunu ve paket dağıtımına dahil edildiğini gösterir. `mypy` veya diğer tip kontrol araçları için önemlidir.



---

claude:


# 📦 Paketleme & Dağıtım Kategorisi

## **setup.py**
Geleneksel Python paket kurulum script'i. Paketin nasıl build edileceğini, hangi dosyaların dahil edileceğini ve bağımlılıkları tanımlar. Modern projeler pyproject.toml'e geçiş yapmakta.

**Tipik içerik:** Package metadata, dependencies, entry points, build requirements. setuptools kütüphanesi kullanılır.

## **pyproject.toml**
Modern Python paket konfigürasyon dosyası (PEP 518). Tüm proje ayarlarını tek bir dosyada toplar: build system, dependencies, tool konfigürasyonları.

**Avantaj:** setup.py, setup.cfg ve diğer tool konfigürasyonlarını tek dosyada birleştirir. Poetry, Flit, Hatch gibi modern build araçları tarafından desteklenir.

## **setup.cfg**
setup.py'nin konfigürasyon dosyası versiyonu. Declarative format kullanır, Python kodu içermez. pyproject.toml öncesi dönemde popülerdi.

**Kullanım:** Metadata, options, ve çeşitli araç konfigürasyonları için kullanılır. INI formatında yazılır.

## **requirements.txt**
Projenin runtime bağımlılıklarını listeleyen basit metin dosyası. pip ile doğrudan kurulum yapılabilir. Sürüm pinleme ve environment yönetimi için kullanılır.

**Format:** `package==1.2.3` veya `package>=1.0,<2.0` şeklinde. pip freeze ile otomatik oluşturulabilir.

## **requirements-dev.txt**
Development ve testing için gerekli olan ek bağımlılıkları içerir. Production'da gerekmeyen araçlar: linting, testing, documentation tools.

**Tipik içerik:** pytest, black, flake8, mypy, sphinx gibi geliştirme araçları. requirements.txt'yi -r ile include eder.

## **Pipfile / Pipfile.lock**
**Pipenv** aracının kullandığı dependency yönetim dosyaları. Pipfile human-readable, Pipfile.lock tam sürüm kilidini içerir.

**Özellik:** Development ve production dependencies ayrımı, Python sürüm yönetimi, deterministic builds için lock dosyası.

## **poetry.lock**
**Poetry** dependency manager'ın oluşturduğu kilit dosyası. Tüm bağımlılıkların tam sürümlerini ve hash'lerini içerir, reproducible builds sağlar.

**Otomatik:** poetry install/add/remove komutları ile otomatik güncellenir. Version control'e commit edilmeli.

## **MANIFEST.in**
Kaynak dağıtımına (sdist) hangi dosyaların dahil edileceğini belirler. setup.py build işleminde kullanılır.

**Kullanım:** Documentation, config dosyaları, data files gibi Python modülleri dışındaki dosyaları paket içine dahil etmek için.

## **py.typed**
Paketinizin type hints içerdiğini ve type checker'lar tarafından kontrol edilebileceğini belirten işaretleyici dosya (PEP 561). İçeriği boş olabilir.

**Amaç:** mypy, PyCharm gibi type checker'ların paketinizi type-safe olarak tanıması. PyPI'da yayınlanan kütüphaneler için önemli.