gpt:


### 🌍 Environment & Config

* **.env / .env.example** → Projenin ortam değişkenlerini saklamak için kullanılır. API anahtarları, veritabanı bağlantıları veya gizli bilgiler burada tanımlanır. `.env.example` dosyası, örnek ortam değişkenlerini paylaşmak için kullanılır.

* **config.ini / config.yaml** → Uygulama konfigürasyonlarını (ayarlar, parametreler) tutmak için kullanılan yapılandırma dosyalarıdır. YAML veya INI formatı, okunabilir ve yönetilebilir olmaları nedeniyle tercih edilir.

* **.python-version** → `pyenv` gibi araçlar için kullanılan dosyadır. Projenin hangi Python sürümünde çalışacağını belirtir ve ortamın tutarlılığını sağlar.


---

claude:

# 🌍 Environment & Config Kategorisi

## **.env / .env.example**
Environment variables dosyaları. Sensitive data, configuration values ve environment-specific settings için güvenli yönetim sağlar.

**.env dosyası:**
- **Sensitive data:** Database passwords, API keys, secret tokens, encryption keys
- **Environment-specific:** DEBUG flags, database URLs, external service endpoints
- **Security:** `.gitignore`'da mutlaka exclude edilmeli, production'a commit edilmemeli
- **Format:** `KEY=value` format, no spaces around equals, comments ile `#`

**.env.example dosyası:**
- **Template:** Required environment variables listesi, actual values olmadan
- **Documentation:** Her variable'ın amacı ve expected format'ı
- **Onboarding:** Yeni developerlar için setup guide, copy to .env instruction
- **Version control:** Git'e commit edilir, team'deki herkes görür

**Popular tools:** python-dotenv kütüphanesi ile .env dosyası otomatik loading.

## **config.ini / config.yaml**
Application configuration dosyaları. Non-sensitive, structured configuration data için kullanılır.

**config.ini (INI format):**
- **Structure:** `[section]` headers ile organized key=value pairs
- **Python integration:** configparser module ile native reading support  
- **Use cases:** Database connection pools, logging levels, feature flags, API endpoints
- **Environment override:** Production/staging/development specific sections

**config.yaml (YAML format):**
- **Hierarchical:** Nested configuration structure, complex data types support
- **Readable:** Human-friendly format, comments support, list/dict structures
- **Modern preference:** JSON alternative, configuration as code approach
- **Validation:** Pydantic, cerberus gibi libraries ile schema validation

**Best practices:** Environment variables override config files, 12-factor app methodology.

## **.python-version**
**pyenv** Python version manager'ın kullandığı dosya. Project-specific Python version requirement belirtir.

**pyenv integration:** 
- **Automatic switching:** Directory'ye girdiğinde otomatik Python version activation
- **Global vs local:** Project-level override, global system Python'dan bağımsız
- **CI/CD consistency:** Development ile production Python version sync

**Format:** `3.11.2` gibi specific version number, single line format.

**Alternative approaches:**
- **asdf:** `.tool-versions` dosyası ile multi-language version management
- **Poetry:** pyproject.toml içinde `requires-python` field
- **pipenv:** Pipfile içinde python_version specification

**Workflow integration:**
```bash
# pyenv kullanım örneği
pyenv install 3.11.2
pyenv local 3.11.2  # .python-version dosyası oluşturur
python --version    # 3.11.2 output'u verir
```

**Team collaboration:** Tüm team members aynı Python version kullanır, version mismatch problems eliminate edilir.