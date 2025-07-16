# 🔧 Path Reference Corrections Summary

## Overview
Comprehensive review and update of all path references throughout the codebase to ensure they align with the current project structure and use the Single Source of Truth (SSOT) configuration system.

## Files Updated

### ✅ Conversion Utilities - Subprocess Calls
**Fixed: Script path references for main conversion modules**

1. **src/utils/conversion/convert_any.py**
   - ❌ OLD: `[sys.executable, 'main.py']`
   - ✅ NEW: `[sys.executable, 'src/core/main.py']`

2. **tools/conversion/convert_any.py**
   - ❌ OLD: `[sys.executable, 'main.py']`
   - ✅ NEW: `[sys.executable, 'src/core/main.py']`

3. **src/utils/conversion/convert_direct.py**
   - ❌ OLD: `[sys.executable, 'main.py']`
   - ✅ NEW: `[sys.executable, 'src/core/main.py']`

4. **tools/conversion/convert_direct.py**
   - ❌ OLD: `[sys.executable, 'main.py']`
   - ✅ NEW: `[sys.executable, 'src/core/main.py']`

5. **src/utils/conversion/convert_fast.py**
   - ❌ OLD: `[sys.executable, 'main_fast.py']`
   - ✅ NEW: `[sys.executable, 'src/core/main_fast.py']`

6. **tools/conversion/convert_fast.py**
   - ❌ OLD: `[sys.executable, 'main_fast.py']`
   - ✅ NEW: `[sys.executable, 'src/core/main_fast.py']`

7. **src/utils/conversion/convert_single.py**
   - ❌ OLD: `C:/Python313/python.exe main.py`
   - ✅ NEW: `C:/Python313/python.exe src/core/main.py`

8. **tools/conversion/convert_single.py**
   - ❌ OLD: `C:/Python313/python.exe main.py`
   - ✅ NEW: `C:/Python313/python.exe src/core/main.py`

### ✅ Batch Processing - Configuration Integration
**Fixed: Default folder references to use SSOT configuration**

9. **src/batch/auto_batch.py**
   - ❌ OLD: `pdf_folder="examples/pdfs", output_folder="outputs/converted_markdown"`
   - ✅ NEW: Uses `config.DEFAULT_PDF_FOLDER` and `config.DEFAULT_CONVERTED_FOLDER`
   - ❌ OLD: `default='pdfs'`, `default='converted_markdown'`
   - ✅ NEW: Uses config paths with proper help text

10. **src/scripts/auto_batch.py**
    - ❌ OLD: `pdf_folder="examples/pdfs", output_folder="outputs/converted_markdown"`
    - ✅ NEW: Uses `config.DEFAULT_PDF_FOLDER` and `config.DEFAULT_CONVERTED_FOLDER`
    - ❌ OLD: `default='pdfs'`, `default='converted_markdown'`
    - ✅ NEW: Uses config paths with proper help text

11. **src/batch/batch_api.py**
    - ❌ OLD: `temp_dir = Path(f"temp_batch/{pdf_name}")`
    - ✅ NEW: `temp_dir = config.DEFAULT_TEMP_FOLDER / f"temp_batch/{pdf_name}"`

### ✅ Core Applications - Output Directory Configuration
**Fixed: Hardcoded output directory creation**

12. **src/core/main.py**
    - ❌ OLD: `output_dir = f"output/{time.strftime('%Y%m%d%H%M%S')}"`
    - ✅ NEW: `output_dir = config.DEFAULT_TEMP_FOLDER / f"output/{time.strftime('%Y%m%d%H%M%S')}"`

13. **src/core/main_fast.py**
    - ❌ OLD: `output_dir = f"output/{time.strftime('%Y%m%d%H%M%S')}_fast"`
    - ✅ NEW: `output_dir = config.DEFAULT_TEMP_FOLDER / f"output/{time.strftime('%Y%m%d%H%M%S')}_fast"`

14. **src/scripts/main.py**
    - ❌ OLD: `output_dir = f"output/{time.strftime('%Y%m%d%H%M%S')}"`
    - ✅ NEW: `output_dir = config.DEFAULT_TEMP_FOLDER / f"output/{time.strftime('%Y%m%d%H%M%S')}"`

15. **src/scripts/main_fast.py**
    - ❌ OLD: `output_dir = f"output/{time.strftime('%Y%m%d%H%M%S')}_fast"`
    - ✅ NEW: `output_dir = config.DEFAULT_TEMP_FOLDER / f"output/{time.strftime('%Y%m%d%H%M%S')}_fast"`

### ✅ Configuration Templates
**Fixed: Default path references in configuration samples**

16. **config/auto_batch_config_sample.py**
    - ❌ OLD: `DEFAULT_PDF_FOLDER = "pdfs"`, `DEFAULT_OUTPUT_FOLDER = "converted_markdown"`
    - ✅ NEW: Commented out with examples showing proper paths and SSOT override note

## SSOT Configuration System Integration

All updated files now properly integrate with the centralized configuration system:

- **Path Resolution**: Uses `config.DEFAULT_PDF_FOLDER`, `config.DEFAULT_CONVERTED_FOLDER`, etc.
- **Proper Imports**: `from config import config`
- **Fallback Handling**: Graceful fallbacks when configuration is not available
- **Type Safety**: Uses `Path` objects for robust path handling

## Benefits of These Changes

1. **Consistency**: All components use the same path resolution system
2. **Maintainability**: Single place to change default paths
3. **Flexibility**: Easy to override paths via environment variables
4. **Correctness**: Scripts now reference correct file locations
5. **Future-Proof**: New project structure properly supported

## Testing Recommendations

After these changes, test the following workflows:

```bash
# Test conversion utilities
python src/utils/conversion/convert_single.py test.pdf
python tools/conversion/convert_direct.py test.pdf

# Test batch processing
python src/batch/auto_batch.py
python src/scripts/auto_batch.py

# Test core applications
cat test.pdf | python src/core/main.py > output.md
```

## Configuration Override Examples

Users can now customize paths via environment variables or configuration files:

```bash
# Environment variables
export DEFAULT_PDF_FOLDER="my_documents"
export DEFAULT_OUTPUT_FOLDER="my_outputs"

# Or via auto_batch_config.py
DEFAULT_PDF_FOLDER = "custom_input"
DEFAULT_OUTPUT_FOLDER = "custom_output"
```

---

**Total Files Updated**: 16 files across conversion utilities, batch processing, core applications, and configuration templates.

**Status**: ✅ All identified path reference issues have been resolved and the codebase now uses the SSOT configuration system consistently.
