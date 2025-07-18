# 🗂️ PDFtoMD - Project Structure
```mermaid
graph TD
 A[pdftomd/] --> B[config.py]
 A --> C[src/]
 A --> D[docs/]
 A --> E[tests/]
 A --> F[tools/]
 A --> G[launcher.py]

 C --> H[core/]
 C --> I[batch/]
 C --> J[scripts/]
 C --> K[utils/]

 D --> L[guides/]
 D --> M[security/]
 D --> N[development/]
 D --> O[legal/]

 style B fill:#4CAF50
 style G fill:#FF9800
 style C fill:#2196F3
 style D fill:#9C27B0
```
## 📁 Current Project Organization

This project follows enterprise-grade organization principles with **Single Source of Truth (SSOT) Configuration** at its core:

```
pdftomd/
├── 🔧 config.py # ⭐ SSOT Configuration System
├── 🔒.env # Environment variables (DO NOT COMMIT)
├── 📋.env.template # Template for.env file
├── 🚀 launcher.py # Universal launcher script
├── 🧪 test_comprehensive.py # Comprehensive test suite
├── 📊 auto_batch_launcher.bat # Windows batch launcher
├── 📄 LICENSE # Apache 2.0 License
├── 📝 README.md # Main documentation
├── 📦 pyproject.toml # Project dependencies & config
└── 🔒 SECURITY_VERIFICATION_COMPLETE.md # Security audit report
```

## 📁 Source Code Structure
```mermaid
graph TB
 subgraph CoreApp ["Core Application"]
 A[src/core/] --> A1[main.py - Single file converter]
 A --> A2[main_fast.py - Fast conversion]
 A --> A3[LLMClient.py - AI interface]
 end

 subgraph BatchProc ["Batch Processing"]
 B[src/batch/] --> B1[auto_batch.py - Main processor]
 B --> B2[batch_api.py - OpenAI Batch API]
 B --> B3[master.py - Management]
 B --> B4[batch_convert.py - Utilities]
 end

 subgraph EntryPoints ["Entry Points"]
 C[src/scripts/] --> C1[Entry point wrappers]
 C --> C2[Backwards compatibility]
 end

 subgraph Utilities ["Utilities"]
 D[src/utils/] --> D1[conversion/ - Converters]
 D --> D2[testing/ - Test tools]
 D --> D3[optimization/ - LM Studio]
 D --> D4[switch_api.py - API switcher]
 end
```

### Core Components

| Directory | Purpose | Key Files |
|---|---|---|
| **📁 src/core/** | Main application logic | `main.py`, `LLMClient.py` |
| **📁 src/batch/** | Batch processing system | `auto_batch.py`, `batch_api.py` |
| **📁 src/scripts/** | Entry point wrappers | Backwards compatibility |
| **📁 src/utils/** | Utility functions | Conversion, testing, optimization |

## 📚 Documentation Structure
```mermaid
graph TB
 A[docs/] --> B[guides/]
 A --> C[security/]
 A --> D[development/]
 A --> E[legal/]

 B --> B1[QUICK_START.md]
 B --> B2[AUTO_BATCH_GUIDE.md]
 B --> B3[SSOT_GUIDE.md]
 B --> B4[LM_Studio_Optimization_Guide.md]

 C --> C1[SECURITY.md]

 D --> D1[PROJECT_STRUCTURE.md]
 D --> D2[IMPLEMENTATION.md]
 D --> D3[CLI_LINTING_CONTROL.md]

 E --> E1[CONTRIBUTORS.md]
 E --> E2[COPYRIGHT]
```
| Documentation Type | Location | Purpose |
|---|---|---|
| **📚 User Guides** | `docs/guides/` | How-to guides for users |
| **🔒 Security** | `docs/security/` | Security policies and procedures |
| **🛠️ Development** | `docs/development/` | Technical documentation |
| **⚖️ Legal** | `docs/legal/` | Licenses and attributions |

## 🧪 Testing Structure
```mermaid
graph LR
 A[tests/] --> B[unit/]
 A --> C[integration/]
 A --> D[samples/]
 A --> E[assets/]

 F[test_comprehensive.py] --> G[11 Test Categories]
 G --> H[100% Pass Rate]
```
| Component | Purpose | Coverage |
|---|---|---|
| **🧪 Comprehensive Suite** | `test_comprehensive.py` | Full system validation |
| **📁 Unit Tests** | `tests/unit/` | Component testing |
| **📁 Integration Tests** | `tests/integration/` | Workflow testing |
| **📁 Test Assets** | `tests/assets/` | Sample files and data |

## 🛠️ Tools & Utilities
```mermaid
graph TD
 A[tools/] --> B[conversion/]
 A --> C[optimization/]
 A --> D[testing/]

 B --> B1[convert_any.py]
 B --> B2[convert_fast.py]

 C --> C1[optimize_lm_studio.py]

 D --> D1[test_openai.py]
 D --> D2[test_batch_api.py]
```

| Tool Category | Purpose | Key Features |
|---|---|---|
| **🔄 Conversion** | File format conversion | Any-to-markdown, fast processing |
| **⚡ Optimization** | Performance tuning | LM Studio optimization |
| **🧪 Testing** | Validation tools | API testing, batch validation |

## 📁 Complete Directory Structure

```
pdftomd/
├── 📁 tools/ # Development tools
│ ├── conversion/ # Conversion tools
│ ├── optimization/ # LM Studio optimization tools
│ └── testing/ # Testing tools
│
├── 📁 config/ # Configuration templates
│ ├── auto_batch_config_sample.py # Batch config template
│ └── templates/ # Additional templates
│
├── 📁 docs/ # Complete documentation
│ ├── README.md # Main documentation
│ ├── QUICK_START.md # 30-second setup guide
│ ├── AUTO_BATCH_GUIDE.md # Complete batch guide
│ ├── IMPLEMENTATION.md # Technical implementation
│ ├── CHANGELOG.md # Version history
│ ├── LM_Studio_Optimization_Guide.md
│ ├── README_zh.md # Chinese documentation
│ └── guides/ # Additional guides
│
├── 📁 tests/ # Test files & test data
│ ├── unit/ # Unit tests (future)
│ ├── integration/ # Integration tests (future)
│ ├── assets/ # Test assets
│ │ └── cases/ # Test case files
│ └── test_util.py # Test utilities
│
├── 📁 examples/ # Example files & demos
│ ├── pdfs/ # Sample PDF files
│ ├── demos/ # Demo images
│ │ ├── demo_01.png
│ │ ├── demo_02.png
│ │ └── pdftomd.png
│ └── outputs/ # Example outputs (future)
│
├── 📁 outputs/ # Generated outputs
│ ├── converted_markdown/ # Batch conversion results
│ └── temp/ # Temporary processing files
│
├── 📄 auto_batch.bat # Windows launcher (updated paths)
├── 📄 pyproject.toml # Project configuration
├── 📄 uv.lock # Dependency lock file
├── 📄 LICENSE # Apache 2.0 License
├── 📄 pyproject.toml # Python project configuration
└── 📄 Makefile # Build configuration
└── 📄 Makefile # Build configuration
```

## 🚀 Quick Start (Updated Paths)

### Auto Batch Processing (Recommended)
```bash
# Windows users - double click:

auto_batch_launcher.bat

# All platforms:

python src/batch/auto_batch.py

# Custom folders:

python src/batch/auto_batch.py "my_pdfs" "my_output"
```
### Single File Processing

```bash

# Core application:

python core/main.py < input.pdf > output.md
python core/main_fast.py < input.pdf > output.md
```

### Utility Scripts

```bash

# Conversion utilities:

python utils/conversion/convert_any.py
python utils/conversion/convert_fast.py

# Test utilities:

python utils/testing/test_openai.py
python utils/testing/simple_llm_test.py

# LM Studio optimization:

python utils/optimization/optimize_lm_studio.py
```

## 📋 Configuration

### Environment Setup

```bash

# Copy configuration template:

cp config/.env.sample.env

# Edit your API keys:

# OPENAI_API_KEY=sk-your-key-here

```

### Auto Batch Configuration

```bash

# Copy batch config template:

cp config/auto_batch_config_sample.py auto_batch_config.py

# Customize settings:

# DEFAULT_PDF_FOLDER = "examples/pdfs"

# DEFAULT_OUTPUT_FOLDER = "outputs/converted_markdown"
```

## 🎯 Benefits of New Organization

### ✅ **Clearer Structure**

- **Core functionality** separated from utilities
- **Batch processing** has its own dedicated space
- **Documentation** centralized and comprehensive
- **Examples and outputs** clearly separated

### ✅ **Easier Navigation**

- **Logical grouping** of related functionality
- **Predictable locations** for different file types
- **Clean root directory** with minimal clutter
- **Dedicated spaces** for different purposes

### ✅ **Better Maintenance**

- **Modular organization** for easier updates
- **Clear separation** of concerns
- **Standardized structure** for team development
- **Future-proof** for additional features

### ✅ **Improved User Experience**

- **Updated batch file** with correct paths
- **Default folders** point to organized locations
- **Clear documentation** hierarchy
- **Simplified setup** process

## 🔄 Migration Notes

### Updated Default Paths:

- **OLD**: `pdfs/` → **NEW**: `examples/pdfs/`
- **OLD**: `converted_markdown/` → **NEW**: `outputs/converted_markdown/`
- **OLD**: `docs/` scattered → **NEW**: `docs/` centralized

### Import Updates:

- Batch scripts now in `batch/` folder
- Utilities organized by category in `utils/`
- Core application in `core/` folder

### Configuration Changes:

- Templates moved to `config/` folder
- Documentation centralized in `docs/`
- Examples separated from working files

## 🛠️ Development Guidelines

### Adding New Features:

1. **Core functionality** → `core/`
2. **Batch processing** → `batch/`
3. **Utility scripts** → `utils/[category]/`
4. **Documentation** → `docs/`
5. **Test files** → `tests/`

### File Organization Rules:

- **Keep root clean** - only essential files
- **Group by function** - related files together
- **Use descriptive folders** - clear purpose
- **Separate data from code** - examples vs source

- --

- **The new structure makes PDFtoMD more professional, maintainable, and user-friendly!** 🎉

For detailed usage instructions, see the [Quick Start Guide](../guides/QUICK_START.md) and [Complete Documentation](../README.md).
