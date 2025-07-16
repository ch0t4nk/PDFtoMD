# 🗂️ MarkPDFDown - Organized Project Structure

## 📁 Project Organization

This project has been completely reorganized for better maintainability, clarity, and ease of use. Here's the new structure with **Single Source of Truth (SSOT) Configuration**:

```
markpdfdown/
├── 🔧 config.py                     # ⭐ SSOT Configuration System
├── 🔒 .env                          # Environment variables (DO NOT COMMIT)
├── 📋 .env.template                 # Template for .env file
├── 🚀 migrate_to_ssot.py           # Migration tool for SSOT
├── 📊 launcher.py                   # Universal launcher script
├── 📄 LICENSE                       # Apache 2.0 License
├── 📝 COPYRIGHT                     # Copyright and attribution notices
├── 👥 CONTRIBUTORS.md               # Project contributors and attributions
│
├── 📁 src/                          # Source code (organized structure)
│   ├── 📁 core/                     # Core application code
│   │   ├── main.py                  # Single-file PDF converter
│   │   ├── main_fast.py             # Fast conversion variant
│   │   └── workers/                 # File processing workers (future)
│   │
│   ├── 📁 batch/                    # Batch processing system (⭐ NEW!)
│   │   ├── auto_batch.py            # Main automated batch processor
│   │   ├── batch_api.py             # OpenAI Batch API interface
│   │   ├── master.py                # Batch management & analytics
│   │   ├── monitor_batch.py         # Real-time monitoring tools
│   │   ├── track_batch_cost.py      # Cost tracking utilities
│   │   └── batch_convert.py         # Batch conversion utilities
│   │
│   ├── 📁 scripts/                  # Standalone scripts
│   │   ├── auto_batch.py            # Entry point for batch processing
│   │   ├── main.py                  # Entry point for single conversion
│   │   ├── main_fast.py             # Entry point for fast conversion
│   │   ├── master.py                # Entry point for batch management
│   │   └── workspace_lint.py        # Workspace linting tool
│   │
│   └── 📁 utils/                    # Utility scripts & tools
│       ├── conversion/              # Various conversion utilities
│       │   ├── convert_any.py       # Any format converter
│       │   ├── convert_direct.py    # Direct conversion
│       │   ├── convert_fast.py      # Fast conversion
│       │   └── convert_single.py    # Single file converter
│       ├── testing/                 # Test utilities
│       │   ├── test_*.py            # Various test scripts
│       │   └── simple_llm_test.py
│       └── combine_pages.py         # Page combination utility
│
├── 📁 tools/                        # External tools & utilities
│   ├── conversion/                  # Conversion tools
│   ├── optimization/                # LM Studio optimization tools
│   └── testing/                     # Testing tools
│
├── 📁 config/                       # Configuration templates
│   ├── auto_batch_config_sample.py  # Batch config template
│   └── templates/                   # Additional templates
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
│ │ └── markpdfdown.png
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
├── 📄 Dockerfile # Docker configuration
└── 📄 Makefile # Build configuration
`
## 🚀 Quick Start (Updated Paths)

### Auto Batch Processing (Recommended)
`bash
# Windows users - double click:

auto_batch.bat

# All platforms:

python batch/auto_batch.py

# Custom folders:

python batch/auto_batch.py "my_pdfs" "my_output"
`
### Single File Processing
`bash
# Core application:

python core/main.py < input.pdf > output.md
python core/main_fast.py < input.pdf > output.md
`
### Utility Scripts
`bash
# Conversion utilities:

python utils/conversion/convert_any.py
python utils/conversion/convert_fast.py

# Test utilities:

python utils/testing/test_openai.py
python utils/testing/simple_llm_test.py

# LM Studio optimization:

python utils/optimization/optimize_lm_studio.py
`
## 📋 Configuration

### Environment Setup
`bash
# Copy configuration template:

cp config/.env.sample.env

# Edit your API keys:

# OPENAI_API_KEY=sk-your-key-here
`
### Auto Batch Configuration
`bash
# Copy batch config template:

cp config/auto_batch_config_sample.py auto_batch_config.py

# Customize settings:

# DEFAULT_PDF_FOLDER = "examples/pdfs"

# DEFAULT_OUTPUT_FOLDER = "outputs/converted_markdown"
`
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

- *The new structure makes MarkPDFDown more professional, maintainable, and user-friendly!** 🎉

For detailed usage instructions, see the [Quick Start Guide](docs/QUICK_START.md) and [Complete Documentation](docs/README.md).
