# File Structure Reorganization Plan

## Current Issues

- Root directory has 50+ files and folders
- Many utility scripts scattered at root level
- Test files mixed with production code
- Documentation files scattered
- Example/demo files at root level

## Proposed New Structure

`
pdftomd/
├── 📁 src/ # Main source code
│ ├── batch/ # Batch processing (existing)
│ ├── core/ # Core functionality (existing)
│ ├── utils/ # Utilities (existing)
│ └── scripts/ # Main entry point scripts
│ ├── auto_batch.py
│ ├── quick_lint.py
│ ├── workspace_lint.py
│ └── cleanup_backups.py
│
├── 📁 config/ # Configuration files (existing)
│ └── auto_batch_config_sample.py
│
├── 📁 docs/ # Documentation (existing + additions)
│ ├── guides/
│ ├── README.md
│ └── [existing docs]
│
├── 📁 examples/ # Examples and demos (existing)
│ ├── demos/
│ ├── outputs/
│ └── pdfs/
│
├── 📁 tests/ # All test files (existing + additions)
│ ├── unit/
│ ├── integration/
│ ├── assets/
│ └── samples/
│ ├── test_sample.md
│ └── test_sample_simple.md
│
├── 📁 tools/ # Development and maintenance tools
│ ├── optimization/
│ │ ├── lm_studio_optimizer.py
│ │ ├── optimize_lm_studio.py
│ │ ├── check_lm_settings.py
│ │ └── find_lm_configs.py
│ ├── conversion/
│ │ ├── convert_any.py
│ │ ├── convert_direct.py
│ │ ├── convert_fast.py
│ │ ├── convert_single.py
│ │ └── combine_pages.py
│ └── testing/
│ ├── test_*.py files
│ └── debug_metadata.py
│
├── 📁 temp/ # Temporary files (new)
│ ├── converted_markdown/
│ ├── outputs/
│ └── batch_requests_*.jsonl
│
├── 📁 legacy/ # Root-level duplicates and legacy files
│ ├── main.py (if different from core/)
│ ├── main_fast.py (if different from core/)
│ └── other duplicates
│
└── 📄 Root files (cleaned up)
 ├── README.md
 ├── LICENSE
 ├── pyproject.toml
 ├── Makefile
 ├──.gitignore
 └── auto_batch.bat (Windows launcher)
`

## Files to Move

### To src/scripts/

- auto_batch.py
- quick_lint.py
- workspace_lint.py
- cleanup_backups.py

### To tools/optimization/

- lm_studio_optimizer.py
- optimize_lm_studio.py
- check_lm_settings.py
- find_lm_configs.py
- optimization_steps.py

### To tools/conversion/

- convert_any.py
- convert_direct.py
- convert_fast.py
- convert_single.py
- combine_pages.py

### To tools/testing/

- test_batch_api.py
- test_config.py
- test_llm_client.py
- test_metadata.py
- test_openai.py
- test_optimized_performance.py
- test_vision_models.py
- debug_metadata.py
- example_metadata_usage.py
- simple_llm_test.py

### To tests/samples/

- test_sample.md
- test_sample_simple.md

### To temp/

- converted_markdown/
- outputs/ (move to examples/outputs/)
- batch_requests_*.jsonl

### To docs/

- AUTO_BATCH_GUIDE.md
- CLI_LINTING_CONTROL.md
- IMPLEMENTATION.md
- IMPLEMENTATION_SUMMARY.md
- ORGANIZATION_PLAN.md
- PROJECT_STRUCTURE.md
- QUICK_START.md
- WORKSPACE_LINTING.md
- CHANGELOG.md

### To legacy/ (check for duplicates first)

- main.py (if different from core/main.py)
- main_fast.py (if different from core/main_fast.py)
- master.py (if different from batch/master.py)
- batch_api.py (if different from batch/batch_api.py)
- batch_convert.py (if different from batch/batch_convert.py)
- monitor_batch.py (if different from batch/monitor_batch.py)
- track_batch_cost.py (if different from batch/track_batch_cost.py)
- switch_api.py (if different from utils/switch_api.py)

## Benefits

1. **Clear separation** of concerns
2. **Easy navigation** - know where to find things
3. **Clean root** - only essential files
4. **Logical grouping** - related files together
5. **Scalable structure** - room for growth
6. **Tool organization** - development vs production code

## Implementation Steps

1. Create new directory structure
2. Move files to appropriate locations
3. Update import paths
4. Update documentation references
5. Test that everything still works
6. Commit the reorganization\n
