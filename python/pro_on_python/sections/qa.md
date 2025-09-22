gpt:


### ✅ Kalite Kontrol & Stil

* **.flake8** → Python kodunu PEP8 standartlarına göre kontrol eden `flake8` aracının ayar dosyasıdır. Hangi uyarıların görüneceği veya hangi dosyaların hariç tutulacağı burada belirlenir.

* **.pylintrc** → `pylint` aracı için yapılandırma dosyasıdır. Kod kalitesi, stil ve hata tespiti ile ilgili kurallar burada tanımlanır.

* **.editorconfig** → Farklı editör ve IDE’lerde ortak kod stili sağlamak için kullanılır. Satır uzunluğu, boşluk karakterleri, dosya sonu boşlukları gibi ayarlar içerir.

* **.pre-commit-config.yaml** → Git commit’leri öncesinde otomatik olarak kod formatlama, lint veya güvenlik kontrolleri yapan pre-commit hook’larını tanımlar.

* **.isort.cfg / pyproject.toml içinde isort ayarları** → Python importlarını alfabetik ve mantıksal sıraya göre düzenleyen `isort` aracının ayarlarıdır.

* **.black.toml / pyproject.toml içinde black ayarları** → Python kodunu standart bir formatta biçimlendiren `black` aracının ayarlarıdır. Kod stilini otomatik olarak uygular.

* **.bandit / .bandit.yml** → Python kodunu güvenlik açıkları açısından tarayan `bandit` aracının ayar dosyasıdır. Riskli kod desenlerini tespit eder.

* **mypy.ini** → Python’da tip denetimi yapan `mypy` aracının yapılandırmasıdır. Hangi dosyaların kontrol edileceği ve hangi kuralların uygulanacağı burada tanımlanır.

* **pyrightconfig.json** → Microsoft’un geliştirdiği `Pyright` tipi denetleyici aracının yapılandırma dosyasıdır. Projeye yönelik tip kontrol ayarlarını JSON formatında belirtir.


---

claude:

# ✅ Kalite Kontrol & Stil Kategorisi

## **.flake8**
**Flake8** linter'ının konfigürasyon dosyası. Python kod kalitesi kontrolü yapar: PEP 8 style violations, unused imports, undefined variables gibi sorunları yakalar.

**Kontrol ettiği alanlar:** Code style, logical errors, cyclomatic complexity, naming conventions, docstring presence.

**Yaygın ayarlar:** Max line length, ignore specific errors, exclude directories, per-file ignores.

## **.pylintrc**
**Pylint** static analysis tool'unun kapsamlı konfigürasyon dosyası. Flake8'den daha detaylı ve strict kod analizi yapar.

**Özellikler:** Code smells detection, refactoring suggestions, design analysis, duplicated code detection, unused variable tracking.

**Konfigürasyon:** Scoring system, message categories (error, warning, info), plugin management, custom checkers.

**Enterprise kullanım:** Büyük kod tabanlarında code quality enforcement için tercih edilir.

## **.editorconfig**
Cross-platform editor konfigürasyon dosyası. Farklı IDE'lerde consistent coding style sağlar: indentation, line endings, charset.

**Desteklenen ayarlar:** indent_style (space/tab), indent_size, end_of_line (lf/crlf), charset (utf-8), trim_trailing_whitespace.

**Editor desteği:** VS Code, PyCharm, Vim, Emacs, Sublime Text gibi major editor'larda otomatik tanınır.

## **.pre-commit-config.yaml**
**Pre-commit** framework'ünün konfigürasyon dosyası. Git commit öncesinde otomatik kod kalite kontrolleri çalıştırır.

**Hooks:** black (formatting), flake8 (linting), mypy (type checking), tests, security scans - hepsini commit öncesi otomatik.

**Workflow:** Kötü kod commit edilmeden önce yakalanır, team-wide code quality enforcement.

**Popüler hooks:** trailing-whitespace, end-of-file-fixer, check-yaml, check-merge-conflict.

## **.isort.cfg / pyproject.toml içinde isort ayarları**
**isort** import sorting tool'unun konfigürasyonu. Python import statement'larını otomatik organize eder.

**Sıralama kriterleri:** Standard library, third-party packages, local imports şeklinde gruplandırma ve alfabetik sıralama.

**Modern approach:** pyproject.toml içinde `[tool.isort]` section'ında configuration. Black ile compatible profile kullanımı yaygın.

## **.black.toml / pyproject.toml içinde black ayarları**
**Black** code formatter'ının konfigürasyon dosyası. "Uncompromising" code formatting ile consistent style sağlar.

**Özellik:** Minimal configuration, opinionated formatting, stable output, automatic code reformatting.

**Yaygın ayarlar:** line-length, target-version, include/exclude patterns, skip-string-normalization.

**Ekosistem uyumu:** isort, flake8, pre-commit ile perfect entegrasyon.

## **.bandit / .bandit.yml**
**Bandit** security linter'ının konfigürasyon dosyası. Python kodunda güvenlik açıklarını ve kötü pratikleri tarar.

**Güvenlik kontrolleri:** SQL injection risks, hardcoded passwords, unsafe YAML loading, shell injection, crypto weaknesses.

**Severity levels:** High, medium, low confidence ratings. False positive management için exclude rules.

**CI/CD integration:** Security-first development için automated security scanning.

## **mypy.ini**
**mypy** static type checker'ının konfigürasyon dosyası. Python'da type annotations kontrolü yapar.

**Type checking:** Function signatures, variable types, return types, generic types validation.

**Strict modes:** Gradual typing support, incremental adoption, strict mode for type safety enforcement.

**IDE integration:** Real-time type error detection, refactoring support, better code completion.

## **pyrightconfig.json**
**Pyright** (Microsoft'un type checker'ı) konfigürasyon dosyası. TypeScript compiler technology'sinden Python'a adapt edilmiş.

**Özellikler:** Fast type checking, VS Code native integration, advanced type inference, strict type checking modes.

**Performance:** mypy'dan daha hızlı, incremental checking, multi-file analysis.

**Modern alternative:** Pylance (VS Code Python extension) backend'i olarak kullanılır.