# Workspace Linting Tools

This directory contains tools to maintain code quality and consistency across the PDFtoMD workspace.

## 🔧 workspace_lint.py

Comprehensive workspace linting tool that fixes common formatting and style issues.

### Usage

```bash

# Run workspace linting

python workspace_lint.py

# Show help

python workspace_lint.py --help
```

### What it does

- **Markdown Files**: Uses `utils.linting.markdown_linter` to fix formatting issues
- **Python Files**: Fixes whitespace, blank lines, and file endings
- **Safety**: Creates `.backup` files before making changes
- **Smart Ignoring**: Skips `outputs/`, `__pycache__/`, and temporary files

### Example Output

```
🔧 PDFtoMD Workspace Linter
============================================================
📁 Scanning workspace: C:\Users\joeyw\pdftomd
🚫 Ignoring:.git, __pycache__, outputs, converted_markdown, temp_batch
============================================================
📊 Found 90 files to process:
 📝 Markdown files:
 🐍 Python files:
📝 Processing Markdown Files...
 Processing: README.md... ✅ 7 fixes applied
 Processing: docs\README.md... ✅ 6 fixes applied

🐍 Processing Python Files...
 Processing: batch\auto_batch.py... ✅ 92 fixes applied
 💾 Backup: auto_batch.py.backup

============================================================
📊 WORKSPACE LINTING SUMMARY
============================================================
📁 Files Processed:
🔧 Total Fixes Applied:
📄 Files with Fixes:
❌ Errors Encountered:
✅ Workspace linting completed with fixes applied!
```

## 🧹 cleanup_backups.py

Simple utility to remove backup files created by the workspace linter.

### Usage

```bash

# Remove all.backup files

python cleanup_backups.py

# Show help

python cleanup_backups.py --help
```

### What it does

- Finds all `.backup` files in the workspace
- Removes them safely
- Shows what was cleaned up

### Example Output

```
🧹 Found 57 backup files to remove:
 🗑️ batch\auto_batch.py.backup
 🗑️ utils\metadata_embedder.py.backup...
✅ Cleaned up 57 backup files!
```

## 🚫 Ignored Directories

The workspace linter automatically ignores:

- `outputs/` - Contains conversion results
- `converted_markdown/` - Session output folders
- `__pycache__/` - Python cache files
- `.git/` - Git repository data
- `node_modules/` - Node.js dependencies
- `venv/`, `env/` - Python virtual environments
- `.vscode/` - Editor settings
- `temp_batch/` - Temporary processing files
- `converted/` - Temporary conversion files

## 📊 Recent Run Statistics

Last run processed:
- **90 total files** (20 Markdown, 70 Python)
- **826 fixes applied** across 47 files
- **0 errors** encountered
- **Safe execution** with backup files created

## 🔄 Recommended Workflow

1. **Before committing**: Run `python workspace_lint.py`
2. **Review changes**: Check that fixes are appropriate
3. **Clean up**: Run `python cleanup_backups.py`
4. **Commit**: Add and commit the cleaned code

## 💡 Integration

These tools integrate with:
- **quick_lint.py**: Individual file linting
- **utils.linting.markdown_linter**: Core markdown linting engine
- **Git workflow**: Safe to run before commits
- **CI/CD**: Can be automated for continuous quality
