gpt:


### 🗑️ Geçici / Otomatik Üretilen Dosyalar

* **\*.pyc** → Python kaynak kodlarının derlenmiş bytecode dosyalarıdır. Performansı artırmak için Python tarafından otomatik üretilir.

* **\*.pyo** → Optimize edilmiş Python bytecode dosyalarıdır. `python -O` ile çalıştırıldığında oluşturulur.

* **\*.pyd** → Windows üzerinde derlenmiş Python extension modüllerini temsil eder (C/C++ ile yazılmış modüller).

* **\*.types** → Bazı tip kontrol araçları (ör. mypy) tarafından oluşturulan tip anotasyonu dosyalarıdır.

* ****pycache**/** → Python’un bytecode cache klasörüdür. `*.pyc` dosyaları burada tutulur.

* **.mypy\_cache/** → `mypy` tip kontrolü sırasında oluşturulan cache klasörüdür. Tip kontrolünü hızlandırır.

* **.pytest\_cache/** → `pytest` test framework’ü tarafından oluşturulan geçici cache klasörüdür. Test sonuçlarının ve konfigurasyonun hızlı erişimi için kullanılır.

* **.coverage / htmlcov/** → Kod coverage araçları tarafından oluşturulan dosya ve rapor klasörleridir. Test kapsamını gösterir.

* **build/** → Paketleme veya derleme sürecinde geçici olarak üretilen dosyaların tutulduğu klasördür.

* **dist/** → Dağıtılabilir paketlerin (`.tar.gz`, `.whl`) oluşturulduğu klasördür.

* **\*.egg-info/** → Paket metadata ve build bilgilerini tutan klasördür. `setuptools` ile paketleme sırasında üretilir.


---

claude:

# 🗑️ Geçici / Otomatik Üretilen Dosyalar Kategorisi

## ***.pyc**
Python bytecode cache dosyaları. Python interpreter'ın source code'u bytecode'a compile ettiği optimize edilmiş dosyalar.

**Amaç:** Startup performance optimization, parse/compile adımını skip ederek faster import times.

**Location:** Python 3.2+ sonrası `__pycache__/` klasörü içinde organize edilir.

**Naming pattern:** `module.cpython-311.pyc` (Python version info içerir)

**Automatic generation:** Python import sırasında otomatik oluşturulur, source code değiştiğinde invalidate edilir.

## ***.pyo**
Python optimized bytecode files. Eski Python versiyonlarında (2.x era) `-O` flag ile oluşturulan optimize edilmiş bytecode.

**Historical:** Python 3.5+ sonrası deprecated, artık `.pyc` files optimization flags içeriyor.

**Legacy systems:** Eski Python deployments'da görülebilir, modern projects'de irrelevant.

## ***.pyd**
Python extension modules (Windows). C/C++ ile yazılmış extension'ların Windows'daki compiled binary formu.

**Platform-specific:** Windows equivalent of `.so` files (Linux shared objects).

**Binary nature:** Machine code, platform ve architecture specific.

**Examples:** NumPy, SciPy gibi performance-critical libraries'in Windows binaries.

## ***.types**
Type information cache files. mypy ve diğer type checker'ların type analysis sonuçlarını cache'lediği dosyalar.

**Performance:** Large codebases'de incremental type checking için speed optimization.

**Temporary:** Type annotations değiştiğinde invalidate edilir, rebuild gerektirir.

## **__pycache__/**
Python 3.2+ sonrası bytecode cache klasörü. Tüm `.pyc` files'ı organize bir şekilde contains eder.

**Hierarchy:** Source code directory structure'ını mirror eder.

**Benefits:** 
- Clean source directories (`.pyc` spam elimination)
- Multiple Python version support (version-specific bytecode)
- Easier cleanup operations

**Size impact:** Large projects'de gigabyte'lara ulaşabilir, disk space consumption.

## **.mypy_cache/**
**mypy** type checker'ın incremental analysis cache'i. Type checking results, dependency graphs, analysis metadata.

**Incremental checking:** Large codebases'de dramatic speed improvement sağlar.

**Content:** Serialized type information, dependency tracking data, error caching.

**Team sharing:** Generally ignored in git, developer-specific optimization.

## **.pytest_cache/**
**pytest** test framework'ünün cache klasörü. Test discovery results, plugin data, performance optimization cache.

**Cache types:**
- **Test collection:** Which tests exist, faster discovery
- **Failed tests:** Last failed tests tracking için `--lf` option
- **Node IDs:** Test identification caching

**Performance:** Test suite startup time optimization, especially large test suites.

## **.coverage / htmlcov/**
**Coverage.py** tool'unun output dosyaları. Code coverage measurement results ve HTML reports.

**.coverage:** Binary coverage data file, SQLite format, coverage run'larının raw data'sı.

**htmlcov/:** HTML coverage report klasörü:
- **index.html:** Main coverage dashboard
- **Source file reports:** Line-by-line coverage visualization  
- **CSS/JS assets:** Interactive reporting UI

**CI/CD integration:** Coverage reports, badge generation, threshold checking için kullanılır.

## **build/**
Package build process'inin temporary files klasörü. setuptools, wheel, distribution building sırasında oluşturulan intermediate files.

**Content:**
- **Compiled extensions:** C/C++ compilation artifacts
- **Temporary source copies:** Build isolation için source duplication
- **Metadata generation:** PKG-INFO, METADATA files

**Build isolation:** Modern build tools (pip, build) isolated environment kullanır.

## **dist/**
Distribution packages'ların output klasörü. Built packages, ready for distribution/upload.

**Package types:**
- **Wheels (.whl):** Binary distribution format, modern standard
- **Source distributions (.tar.gz):** Source code packages
- **Eggs (.egg):** Legacy format, deprecated

**PyPI upload:** `twine upload dist/*` ile PyPI'a package publishing.

## ***.egg-info/**
Setuptools metadata klasörü. Package metadata, dependency information, entry points.

**Content:**
- **PKG-INFO:** Package metadata (name, version, description)
- **requires.txt:** Runtime dependencies
- **entry_points.txt:** Console scripts, plugin entry points  
- **SOURCES.txt:** Package file listing

**Modern alternative:** `.dist-info/` format, wheel standard ile standardize edildi.
