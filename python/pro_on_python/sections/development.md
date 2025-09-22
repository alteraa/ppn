gpt:

### 💻 Development & IDE

* **.vscode/** → Visual Studio Code için proje bazlı ayarların, eklenti konfigürasyonlarının ve workspace ayarlarının bulunduğu klasördür. Launch konfigurasyonları, formatter ve linter ayarları gibi bilgiler burada saklanır.

* **.idea/** → JetBrains IDE’leri (PyCharm, IntelliJ IDEA vb.) için proje ayarlarını, kod stili ve workspace bilgilerini tutan klasördür. Kod tamamlama, debugger ve proje yapısı gibi ayarları içerir.

---

claude:

# 💻 Development & IDE Kategorisi

## **.vscode/**
**Visual Studio Code** IDE'sinin project-specific ayarlarını içeren klasör. Team-wide consistent development environment sağlar.

**Ana dosyalar:**
- **settings.json:** Workspace-specific VS Code ayarları, Python interpreter path, formatter settings
- **extensions.json:** Recommended extensions listesi, team members için automatic suggestions
- **launch.json:** Debug configurations, breakpoint settings, environment variables
- **tasks.json:** Custom build/run tasks, terminal commands automation

**Python-specific configurations:**
```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "editor.formatOnSave": true
}
```

**Team benefits:** Onboarding acceleration, consistent code style, shared debug configurations, automatic extension installation.

**Best practices:** Commit to git for team sharing, avoid user-specific paths, use relative paths for portability.

## **.idea/**
**JetBrains IDEs** (PyCharm, IntelliJ IDEA) project konfigürasyon klasörü. IDE-specific project metadata ve ayarları içerir.

**Önemli dosyalar:**
- **misc.xml:** Python interpreter, project structure settings
- **modules.xml:** Project module definitions, source root mappings  
- **vcs.xml:** Version control system integration settings
- **inspectionProfiles/:** Code quality inspection rules, custom inspection settings
- **runConfigurations/:** Run/debug configurations, test runners

**PyCharm-specific features:**
- **Database integration:** Database tool window, SQL console configurations
- **Remote development:** Remote interpreter setup, deployment configurations
- **Code style:** Team-wide code style schemes, import optimization rules

**Gitignore considerations:**
```gitignore
# JetBrains IDEs
.idea/
# But keep some team-shared configs
!.idea/codeStyles/
!.idea/inspectionProfiles/
!.idea/runConfigurations/
```

**Workspace sharing:** Selective commit için team-wide settings vs personal preferences separation.

**Professional features:** Advanced debugging, profiling, database tools, deployment automation, collaborative development tools.