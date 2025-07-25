# 📝 Changelog

## Version: 4.1.0 - Comprehensive Workspace Cleanup (July 25, 2025)

### 🧹 **MAJOR CODEBASE CLEANUP**

* **REMOVED**: 16 duplicate files via proper git operations
 - `src/scripts/main.py` & `src/scripts/main_fast.py` (kept canonical in `src/core/`)
 - `src/scripts/auto_batch.py` & `src/scripts/master.py` (kept canonical in `src/batch/`)
 - `src/scripts/cleanup_backups.py` (functionality centralized)
 - Entire `src/utils/conversion/` directory (duplicated from `tools/conversion/`)
 - 6 backup/duplicate files from `tools/conversion/`

* **NEW**: Centralized utilities created
 - `src/utils/cleanup_manager.py` - Consolidates cleanup functionality from 6+ scattered files
 - `src/utils/markdown_cleaner.py` - Unifies markdown processing functions

* **UPDATED**: Files modernized to use centralized utilities
 - `src/batch/batch_api.py` - Now uses centralized CleanupManager with fallback
 - `launcher.py` - Updated to reflect new file structure and available tools

### 📊 **IMPACT METRICS**

* **ELIMINATED**: ~500+ lines of duplicated code across the codebase
* **CENTRALIZED**: All cleanup functionality into reusable CleanupManager class
* **UNIFIED**: Markdown processing functions into single utility module
* **MAINTAINED**: Clean git history with proper git rm operations

### 🆕 **ENHANCED ARCHITECTURE**

* **CENTRALIZED**: All cleanup operations now use unified `CleanupManager`
* **IMPROVED**: Markdown processing with comprehensive cleaning functions
* **UPDATED**: Launcher system reflects current file structure
* **ENHANCED**: Documentation updated to reflect cleanup results

- --

## Version: 4.0.0 - Security & Documentation Overhaul (July 16, 2025)

### 🔒 **CRITICAL SECURITY UPDATES**

* **FIXED**: Complete security audit and vulnerability remediation
* **FIXED**: Eliminated hardcoded API key exposure in source code
* **FIXED**: Removed malicious HTTP headers from supply chain attack
* **FIXED**: Secured.env backup files and enhanced gitignore protection
* **VERIFIED**: GitHub repository confirmed clean - no API key exposure
* **NEW**: Comprehensive security verification documentation

### 🧪 **TESTING & QUALITY ASSURANCE**

* **NEW**: Comprehensive test suite with 100% pass rate (11/11 tests)
* **NEW**: GitHub Actions CI/CD pipeline for automated testing
* **NEW**: Cross-platform compatibility validation (Windows/Linux/macOS)
* **NEW**: Enterprise-grade quality assurance processes
* **NEW**: Security-integrated testing workflows

### 📚 **DOCUMENTATION ENHANCEMENT**

* **UPDATED**: All documentation reflects current project state and structure
* **NEW**: Added Mermaid diagrams for visual architecture representation
* **NEW**: Enhanced README with flowcharts, tables, and interactive elements
* **UPDATED**: Corrected all file paths and links throughout documentation
* **NEW**: Comprehensive guide cross-references and navigation
* **UPDATED**: Installation instructions with multiple package managers

- --

# Version: 3.1.0 - Documentation Reorganization & Project Updates

## 📚 **DOCUMENTATION REORGANIZATION**

### 🗂️ **STRUCTURED DOCUMENTATION SYSTEM**

* **NEW**: Organized documentation into structured subdirectories
 - `docs/guides/`: User-facing guides (QUICK_START, AUTO_BATCH_GUIDE, SSOT_GUIDE, LM_Studio)
 - `docs/security/`: Security documentation (SECURITY.md)
 - `docs/development/`: Technical and development documentation
 - `docs/legal/`: Legal and attribution files (CONTRIBUTORS, COPYRIGHT)
* **NEW**: Clean root directory - moved all documentation to organized docs/ structure
* **NEW**: Updated all internal documentation links to reflect new structure
* **NEW**: Git history preserved using `git mv` commands for all file moves

### 🔗 **LINK MAINTENANCE & PATH UPDATES**

* **UPDATED**: All documentation cross-references now use correct relative paths
* **UPDATED**: README.md updated with correct `src/batch/auto_batch.py` paths
* **UPDATED**: AUTO_BATCH_GUIDE.md updated with current project structure
* **UPDATED**: PROJECT_STRUCTURE.md reflects current organization
* **UPDATED**: Repository URLs updated from original to `ch0t4nk/PDFtoMD`

### 🛠️ **PROJECT STATE SYNCHRONIZATION**

* **UPDATED**: Documentation now accurately reflects current file structure
* **UPDATED**: All command examples use correct paths (`src/batch/` instead of `batch/`)
* **UPDATED**: Launcher references updated to `auto_batch_launcher.bat`
* **VERIFIED**: All documentation links functional and pointing to existing files

- --

# Version: 3.0.0 - Single Source of Truth (SSOT) Configuration System

## 🔧 MAJOR SECURITY & CONFIGURATION OVERHAUL

### 🔒 **CRITICAL SECURITY IMPROVEMENTS**

* **NEW**: Single Source of Truth (SSOT) configuration system via `config.py`
* **NEW**: Centralized API key management - keys never hardcoded in source files
* **NEW**: Secure `.env` template system for sharing configuration structure
* **NEW**: API key removed from git history - complete security audit and cleanup
* **NEW**: Environment switching support (development/production/LM Studio)

### 🎯 **CENTRALIZED CONFIGURATION MANAGEMENT**

* **NEW**: `config.py` - Complete SSOT system managing all settings from one location
* **NEW**: `.env.template` - Secure template for environment variable setup
* **NEW**: `migrate_to_ssot.py` - Automated migration tool for existing installations
* **NEW**: All 35 Python files migrated to use centralized configuration (193 changes)
* **NEW**: Eliminated all hardcoded paths and scattered os.getenv() calls

### 📁 **COMPREHENSIVE SETTINGS MANAGEMENT**

* **NEW**: API Configuration (key, base URL, model selection)
* **NEW**: Directory Management (PDF input, outputs, temp, config folders)
* **NEW**: Processing Settings (temperature, max tokens, DPI, timeouts)
* **NEW**: Cost Management (warning/alert thresholds, tracking)
* **NEW**: Feature Flags (linting, metadata, cleanup, session organization)

### 🛡️ **SECURITY FEATURES**

* **NEW**: API keys isolated to `.env` file only - never in source code
* **NEW**: `.env` in `.gitignore` - never committed to version control
* **NEW**: Template system for secure configuration sharing
* **NEW**: Git history cleaned of exposed API keys
* **NEW**: Migration from legacy environment variable setup

### 🚀 **MIGRATION & COMPATIBILITY**

* **NEW**: Automated migration tool updates all existing code
* **NEW**: Backward compatibility maintained for existing workflows
* **NEW**: All import paths updated for new `src/` structure
* **NEW**: Launcher system enhanced for SSOT integration

- --

# Version: 2.0.0 - Auto Batch Processing

## 🚀 Major New Features

### 🤖 Auto Batch Processing System

* **NEW**: Complete automation workflow with `auto_batch.py` - zero interaction required
* **NEW**: OpenAI Batch API integration with **50% cost savings** compared to standard API
* **NEW**: Windows batch file wrapper (`auto_batch.bat`) for easy double-click execution
* **NEW**: Real-time progress monitoring with intelligent status checking
* **NEW**: Session-based output organization with timestamped folders
* **NEW**: Comprehensive cost analysis and usage tracking per document and per page

### 💰 Cost Optimization & Analytics

* **NEW**: Detailed cost estimation before processing (prevents surprises)
* **NEW**: Per-page cost analysis with token usage breakdown
* **NEW**: Cost comparison reports showing Batch API vs Standard API savings
* **NEW**: Configurable cost alert thresholds ($1.00 warning, $5.00 alert)
* **NEW**: Usage statistics export to JSON for accounting/analysis

### 🔧 Enhanced Configuration & Management

* **NEW**: `auto_batch_config_sample.py` - Template for customizing processing settings
* **NEW**: `master.py` - Comprehensive batch management and cleanup utilities
* **NEW**: `monitor_batch.py` - Standalone batch monitoring tool
* **NEW**: `track_batch_cost.py` - Real-time cost tracking during processing
* **NEW**: Automatic cleanup of temporary files and batch artifacts

### 📊 Improved Quality & Prompting

* **ENHANCED**: Advanced prompting system with temperature 0.05 for consistency
* **ENHANCED**: 9-point conversion requirements for better markdown output
* **ENHANCED**: Expert-level document conversion prompts eliminating "ugly" formatting
* **ENHANCED**: Maximum 8192 tokens per request for comprehensive page coverage
* **ENHANCED**: 69% more content generation compared to previous versions

### 🗂️ Output Organization

* **NEW**: Session folders with format `session_YYYYMMDD_HHMMSS`
* **NEW**: Automatic `README.md` generation with session summary
* **NEW**: `cost_analysis.json` with detailed financial breakdown
* **NEW**: Organized file structure separating markdown files from metadata

### 🔄 Batch Management Features

* **NEW**: Automatic batch status monitoring (validating → in_progress → completed)
* **NEW**: Resume capability for interrupted batches
* **NEW**: Comprehensive error handling and retry logic
* **NEW**: Background processing support for long-running operations
* **NEW**: Detailed logging and audit trail for all operations

## 📈 Performance Improvements

* **IMPROVED**: Processing speed through optimized batch request grouping
* **IMPROVED**: Cost efficiency - $0.005 per page average (down from ~$0.010)
* **IMPROVED**: Token utilization with smarter request batching
* **IMPROVED**: Memory usage through streaming page extraction

## 🛠️ Technical Enhancements

* **NEW**: Complete Python 3.13.3 compatibility testing
* **NEW**: Enhanced error messages and user guidance
* **NEW**: Robust file path handling for Windows/Unix systems
* **NEW**: Intelligent PDF page extraction with DPI optimization
* **NEW**: Advanced batch file upload/download management

## 📚 Documentation

* **NEW**: `AUTO_BATCH_GUIDE.md` - Comprehensive guide with API reference
* **NEW**: `QUICK_START.md` - 30-second setup guide
* **UPDATED**: Main README with auto-batch feature prominence
* **NEW**: Troubleshooting guides and performance optimization tips

## 🧪 Testing & Validation

* **NEW**: Complete clean-slate testing with artifact cleanup
* **NEW**: Cost validation against estimates (within 5% accuracy)
* **NEW**: End-to-end workflow testing from PDF discovery to organized output
* **NEW**: Performance benchmarking for 93-page batch (3.6 minutes total time)

- --

# Version: 1.0.8

* [#15](https://github.com/MarkPDFdown/markpdfdown/pull/15): fix: Fixed the issue where hunyuan does not support empty system_prompt

# Version: 1.0.7

* [#8](https://github.com/MarkPDFdown/markpdfdown/pull/8): fix: Fix the path spelling error in the Readme
* [#11](https://github.com/MarkPDFdown/markpdfdown/pull/11): fix: Fix the OpenAI API 400 Bad Request issue #10

### Changelog

All notable changes to this project will be documented in this file. Dates are displayed in UTC.

Generated by [`auto-changelog`](https://github.com/CookPete/auto-changelog).

#### [1.0.6](https://github.com/jorben/markpdfdown/compare/1.0.5...1.0.6)

> 24 March
- chore: Compress demo images [`9062d01`](https://github.com/jorben/markpdfdown/commit/9062d01644ac098da41c9f4450b1217d9728e2b3)
- chore: Emphasize the use of LaTeX syntax for mathematical formulas [`2aef544`](https://github.com/jorben/markpdfdown/commit/2aef5448cece60efbc03d40ad5d05b7d5e9877d1)
- chore: Add ChangeLog action [`3587a00`](https://github.com/jorben/markpdfdown/commit/3587a007c242b857586b2beb8a1e105743713a45)

#### [1.0.5](https://github.com/jorben/markpdfdown/compare/1.0.4...1.0.5)

> 22 March
- refactor: Refactor PDFWorker, build a FileWorker base class to facilitate future extension for supporting more file types [`d4e6398`](https://github.com/jorben/markpdfdown/commit/d4e6398e9ea0f59d1c512b9e35ef5efc2fd117cd)
- feat: Added support for converting images (JPG/PNG/BMP) to Markdown #6 [`1eab0db`](https://github.com/jorben/markpdfdown/commit/1eab0db854ba8669d8107edf74aac645430f71d0)

#### [1.0.4](https://github.com/jorben/markpdfdown/compare/1.0.3...1.0.4)

> 20 March
- chore: Add Chinese introduction [`d1a9a69`](https://github.com/jorben/markpdfdown/commit/d1a9a69f60b378e1f899fcc7c874ab1ae185edf5)
- feat: Add and remove markdown wrapping and corresponding unit test cases [`c75fb71`](https://github.com/jorben/markpdfdown/commit/c75fb71f9e8ed0db781fbba93ce27050ef3c097d)
- chore: Modify Readme [`b6c0208`](https://github.com/jorben/markpdfdown/commit/b6c020859a570731e9a31ddf8e1de618eeeba2b2)

#### [1.0.3](https://github.com/jorben/markpdfdown/compare/1.0.2...1.0.3)

> 15 March
- chore: The default settings are for the OpenAI API and the GPT-4 model. [`5f0bef0`](https://github.com/jorben/markpdfdown/commit/5f0bef0d04fe83b79a188385613d84b2d6bf1c5f)
- chore: Add effect demonstration images to the Readme [`cb6e317`](https://github.com/jorben/markpdfdown/commit/cb6e317c2247f8df9572f26dc758f8faa7e5280f)
- fix: Fix the "the input device is not a TTY" error in docker run [`4359f4b`](https://github.com/jorben/markpdfdown/commit/4359f4b21ee0d5460b110db36809f689d5367264)

#### [1.0.2](https://github.com/jorben/markpdfdown/compare/1.0.1...1.0.2)

> 15 March
- fix: Fix the build image pipeline error on the armv7 platform [`afa0f61`](https://github.com/jorben/markpdfdown/commit/afa0f6191413166bc8ed2ad28db2defd40d0d199)

#### [1.0.1](https://github.com/jorben/markpdfdown/compare/1.0.0...1.0.1)

> 15 March
- fix: Fix the build image pipeline error on the 386 platform [`7012440`](https://github.com/jorben/markpdfdown/commit/7012440a3a0af55a901ca5bad6495a05a4509456)

####
> 15 March
- Initial commit [`58eac07`](https://github.com/jorben/markpdfdown/commit/58eac0798ec6ea4b521ddc060284489e27a42ca0)
- chore: Updated some content [`8f5c533`](https://github.com/jorben/markpdfdown/commit/8f5c5339a6ca5690266f2a97223c410b4ef6b168)
- chore: Add LLMClient, PDFWork class and implementation [`b040a48`](https://github.com/jorben/markpdfdown/commit/b040a4878957f76baa51db4f958b52b1eeb1bb38)\n
