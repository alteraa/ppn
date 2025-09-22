gpt:

### 🔒 Güvenlik & Analiz

* **safety-policy.json** → Projedeki güvenlik açıklarının raporlanması ve yönetilmesi için kullanılan bir yapılandırma dosyasıdır. `safety` aracı ile Python paketlerinin bilinen güvenlik açıklarını taramak ve politika kurallarını uygulamak için kullanılır.

* **.snyk** → `Snyk` güvenlik platformu tarafından kullanılan konfigürasyon dosyasıdır. Projenin bağımlılıklarını analiz ederek güvenlik açıklarını bulur ve raporlar. Ayrıca, hangi açıkların ignore edileceği veya hangi policy’nin geçerli olacağı gibi bilgileri içerir.

---

claude:

# 🔒 Güvenlik & Analiz Kategorisi

## **safety-policy.json**
**Safety** aracının policy konfigürasyon dosyası. Python dependency'lerindeki bilinen güvenlik açıklarını (CVE) tarar ve policy-based filtering yapar.

**Özellikler:** Known vulnerability database kontrolü, severity-based filtering, ignore rules for false positives, compliance reporting.

**Database:** PyUp.io security database kullanır, sürekli güncellenen CVE listesi ile dependency scanning.

**Policy management:** Hangi seviyedeki güvenlik açıklarının ignore edileceği, hangi paketlerin whitelist'te olduğu gibi kuralları tanımlar.

**CI/CD integration:** Automated security scanning pipeline'ında kullanılır, vulnerable dependencies build'i fail edebilir.

## **.snyk**
**Snyk** vulnerability management platform'unun konfigürasyon dosyası. Comprehensive security scanning ve policy enforcement sağlar.

**Tarama alanları:** 
- **Dependencies:** Known vulnerabilities in packages
- **Code:** Static analysis for security issues  
- **Container:** Docker image vulnerability scanning
- **Infrastructure as Code:** Terraform, Kubernetes config security

**Policy features:** Custom ignore rules, severity thresholds, license compliance checking, fix suggestions.

**Enterprise integration:** GitHub/GitLab security tab integration, developer-first security workflow, automated pull request fixes.

**Reporting:** Detailed vulnerability reports, risk scoring, compliance dashboards, trend analysis.

**Modern approach:** Shift-left security strategy ile development process'e entegre güvenlik kontrolü.