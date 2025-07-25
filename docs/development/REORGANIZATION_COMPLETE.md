# PDFtoMD - Reorganized File Structure

## Directory Structure

After reorganization, the project now has a clean, logical structure:
`text
pdftomd/
├── src/ # Core source code
│ ├── batch/ # Batch processing modules
│ ├── core/ # Core functionality (workers, clients)
│ ├── utils/ # Utility modules (conversion, linting, etc.)
│ └── scripts/ # Main executable scripts
├── tools/ # Standalone tools
│ ├── conversion/ # File conversion tools
│ ├── optimization/ # LM Studio optimization tools
│ └── testing/ # Testing and debugging tools
├── docs/ # All documentation
├── config/ # Configuration templates
├── temp/ # Temporary files and workspace
├── tests/ # Unit and integration tests
├── examples/ # Example files and demos
├── outputs/ # Generated output files
└── pdfs/ # Input PDF files
```
## Quick Access

Use the `launcher.py` script for easy access to tools:
`bash

# Main batch processing

python launcher.py auto-batch --help

# Workspace maintenance

python launcher.py workspace-lint

# Quick utilities

python launcher.py quick-lint
python launcher.py cleanup
python launcher.py convert-any input.pdf
python launcher.py optimize-lm
`

## Key Scripts

### Main Processing

- `src/scripts/auto_batch.py` - Enhanced main batch processor with CLI options
- `src/scripts/main.py` - Original main entry point
- `src/scripts/main_fast.py` - Fast processing entry point

### Workspace Tools

- `src/scripts/workspace_lint.py` - Comprehensive workspace linting
- `src/scripts/quick_lint.py` - Quick linting utility
- `src/scripts/cleanup_backups.py` - Backup file management

### Conversion Tools

- `tools/conversion/convert_any.py` - Universal file converter
- `tools/conversion/convert_fast.py` - Fast conversion utility
- `tools/conversion/convert_single.py` - Single file converter

### Optimization Tools

- `tools/optimization/optimize_lm_studio.py` - LM Studio optimizer
- `tools/optimization/check_lm_settings.py` - Settings checker

### Testing Tools

- `tools/testing/simple_llm_test.py` - LLM connection test
- `tools/testing/debug_metadata.py` - Metadata debugging

## Features

### CLI Options (auto_batch.py)

- `--no-lint` or `--skip-lint` - Skip linting for faster processing
- `--no-metadata` - Skip metadata generation
- `--help` - Show all available options

### Workspace Linting

- Processes 90+ files across the workspace
- Fixes markdown and Python formatting issues
- Ignores output directories to avoid changing generated files
- Creates backup files for safety

### File Organization Benefits

- **Clean root directory** - Only essential config files remain
- **Logical grouping** - Related functionality grouped together
- **Easy navigation** - Clear hierarchy for finding files
- **Tool separation** - Standalone tools separate from core code
- **Improved maintainability** - Better organization for development

## Migration Notes

All import paths have been updated to reflect the new structure. The reorganization preserves git history through proper `git mv` operations.\n
