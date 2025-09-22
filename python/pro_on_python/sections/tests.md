gpt:


### 🧪 Test & Örnekler

* **tests/** → Projenin birim testleri ve entegrasyon testlerinin saklandığı ana klasördür. Genellikle `pytest` veya `unittest` ile yazılmış test dosyaları içerir.

* **conftest.py** → `pytest` ile ortak fixture ve hook’ların tanımlandığı dosyadır. Testler arasında paylaşılan setup/teardown işlemleri burada yapılır.

* **pytest.ini** → `pytest` test framework’ünün yapılandırma dosyasıdır. Test discovery, marker tanımları ve test parametreleri burada belirlenir.

* **coverage.rc** → Kod kapsama (coverage) araçları için yapılandırma dosyasıdır. Hangi dosyaların ölçüleceği, hangi dosyaların hariç tutulacağı gibi ayarlar içerir.

* **.hypothesis/** → `Hypothesis` kütüphanesi ile property-based testing yapılırken oluşturulan cache ve ayar klasörüdür. Testlerin deterministik ve tekrar edilebilir olmasını sağlar.

* **examples/** → Projenin kullanımını gösteren örnek kodlar veya scriptlerin bulunduğu klasördür. Kullanıcıların ve geliştiricilerin projeyi hızlıca anlamasına yardımcı olur.


---

claude:

# 🧪 Test & Örnekler Kategorisi

## **tests/**
Test dosyalarının organize edildiği ana klasör. Unit tests, integration tests, end-to-end tests gibi tüm test türlerini içerir.

**Tipik yapı:** Test dosyaları `test_` prefix'i veya `_test` suffix'i kullanır. Module structure ana kod ile parallel organize edilir.

**Test türleri:** Unit tests (isolated component testing), integration tests (component interactions), functional tests (user scenarios).

**Best practice:** Source code ile aynı klasör yapısını mirror eden test organization, easy navigation ve maintenance sağlar.

## **conftest.py**
**pytest** framework'ünün konfigürasyon ve fixture dosyası. Test session'ları arasında paylaşılan setup/teardown logic'ini içerir.

**Fixtures:** Database connections, mock objects, test data, temporary files gibi reusable test components tanımlar.

**Scope management:** session, module, class, function level fixture'lar ile resource lifecycle yönetimi.

**Plugin integration:** pytest plugin'leri ve custom hooks için konfigürasyon noktası.

**Hierarchy:** Her test directory kendi conftest.py'sine sahip olabilir, inheritance hierarchy sağlar.

## **pytest.ini**
**pytest** test runner'ının ana konfigürasyon dosyası. Test discovery, reporting, plugin settings gibi global ayarları içerir.

**Test discovery:** Test file patterns, directory inclusion/exclusion rules, test collection behavior.

**Reporting:** Verbose output, custom markers, test result formatting, failure reporting options.

**Plugin configuration:** Third-party pytest plugin'leri için settings (pytest-cov, pytest-xdist, pytest-mock).

**Markers:** Custom test markers (@pytest.mark.slow, @pytest.mark.integration) tanımlama ve filtering.

## **coverage.rc**
**Coverage.py** aracının konfigürasyon dosyası. Code coverage measurement ve reporting ayarlarını içerir.

**Coverage types:** Line coverage, branch coverage, function coverage measurement strategies.

**Reporting:** HTML, XML, JSON format reports, threshold settings, coverage badges için data export.

**Exclusions:** Test files, generated code, unreachable code blocks için coverage exclusion rules.

**CI/CD integration:** Minimum coverage thresholds, fail-under settings, automated coverage reporting.

## **.hypothesis/**
**Hypothesis** property-based testing kütüphanesinin database ve cache klasörü. Test case generation history ve performance optimization data içerir.

**Property-based testing:** Random input generation ile comprehensive test coverage, edge case discovery.

**Test case database:** Previously found failing examples, regression prevention, minimal failing cases.

**Performance cache:** Strategy optimization, test generation speed improvement için cached data.

**Reproducibility:** Deterministic test failures için seed management ve example replay.

## **examples/**
Projenin kullanımını gösteren örnek kod ve tutorial'ların bulunduğu klasör. Documentation'ı destekleyen practical use cases içerir.

**İçerik türleri:** 
- **Basic usage:** Simple API usage examples
- **Advanced patterns:** Complex scenarios, best practices
- **Tutorials:** Step-by-step learning materials
- **Notebooks:** Jupyter notebooks ile interactive examples

**Organization:** Use case based klasör yapısı, beginner'dan advanced'e doğru progression.

**Testing:** Examples'lar da test edilmeli, broken examples documentation güvenilirliğini azaltır.

**Integration:** Documentation tools (Sphinx, MkDocs) ile entegrasyon, automated example testing.

