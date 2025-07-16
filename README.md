# MarkPDFDown

**English**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub stars](https://img.shields.io/github/stars/ch0t4nk/PDFtoMD)](https://github.com/ch0t4nk/PDFtoMD/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ch0t4nk/PDFtoMD)](https://github.com/ch0t4nk/PDFtoMD/network)

Enterprise-ready PDF to Markdown conversion tool powered by multimodal AI. Features secure SSOT configuration, centralized API key management, comprehensive security controls, and enterprise-grade batch processing capabilities.

![markpdfdown](https://raw.githubusercontent.com/ch0t4nk/PDFtoMD/master/examples/demos/markpdfdown.png)

## Overview

MarkPDFDown is designed to simplify the process of converting PDF documents into clean, editable Markdown text for enterprise environments. By utilizing advanced multimodal AI models with enterprise-grade security and configuration management, it can accurately extract text, preserve formatting, and handle complex document structures including tables, formulas, and diagrams.

## Enterprise Features

- **🔧 Single Source of Truth (SSOT) Configuration** - Centralized configuration management for enterprise deployments
- **🔒 Enterprise Security Framework** - Secure API key management, git history protection, and compliance features
- **👥 Team Collaboration Ready** - Multi-user support with secure onboarding procedures
- **📊 Cost Management & Analytics** - Detailed cost tracking and budget controls for enterprise use
- **⚙️ Production-Ready Architecture** - Robust error handling, logging, and monitoring capabilities

## Features

- **PDF to Markdown Conversion**: Transform any PDF document into well-formatted Markdown
- **Image to Markdown Conversion**: Transform image into well-formatted Markdown
- **🤖 Auto Batch Processing**: Fully automated batch conversion with OpenAI Batch API (50% cost savings)
- **🔧 Local Linting System**: Super-fast local markdown formatting and cleanup (no API costs)
- **Multimodal Understanding**: Leverages AI to comprehend document structure and content
- **Format Preservation**: Maintains headings, lists, tables, and other formatting elements
- **💰 Cost Optimization**: Advanced cost tracking and optimization with detailed analytics
- **📊 Progress Monitoring**: Real-time batch processing status and intelligent monitoring
- **� Clean Output Structure**: Organized converted/, metadata/, temp/ folder structure
- **🧹 Automatic Cleanup**: Smart temp file management and old file removal
- **Customizable Model**: Configure the model to suit your needs

## Demo
![Demo Image](https://raw.githubusercontent.com/ch0t4nk/PDFtoMD/master/examples/demos/demo_02.png)

## Installation

### Using uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/ch0t4nk/PDFtoMD.git
cd PDFtoMD

# Install dependencies and create virtual environment
uv sync
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/ch0t4nk/PDFtoMD.git
cd PDFtoMD

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install production dependencies
pip install -r requirements.txt

# OR install development dependencies (includes testing tools)
pip install -r requirements-dev.txt
```

### Using conda

```bash
conda create -n markpdfdown python=3.9
conda activate markpdfdown

# Clone the repository
git clone https://github.com/ch0t4nk/PDFtoMD.git
cd PDFtoMD

# Install dependencies
pip install -r requirements.txt
```
## Usage

### 🔧 Initial Setup (REQUIRED)

**Before first use, configure your API key using our secure SSOT system:**

```bash
# 1. Copy the template to create your .env file
cp .env.template .env

# 2. Edit .env and add your OpenAI API key
# OPENAI_API_KEY="sk-your-actual-api-key-here"

# 3. Test configuration
python config.py
```

✅ **Security Features:**
- 🔒 API keys never stored in source code
- 📋 Template system for easy setup  
- 🎯 Single Source of Truth for all settings
- 🔄 Easy environment switching (dev/prod/local)
- 🛡️ Git history cleaned of any exposed keys

See the [SSOT Configuration Guide](docs/guides/SSOT_GUIDE.md) and [Security Guide](docs/security/SECURITY.md) for complete setup documentation.

### 🤖 Auto Batch Processing (Recommended)

For processing multiple PDFs with **50% cost savings** using OpenAI Batch API:
```bash
# Quick start - process all PDFs in examples/pdfs/ folder

python src/batch/auto_batch.py

# Custom folders

python src/batch/auto_batch.py documents outputs

# Windows users can double-click

auto_batch_launcher.bat
```
- **Batch Processing Features:**
- ✅ Fully automated workflow (set it and forget it)
- 💰 50% cost savings with OpenAI Batch API
- 📊 Real-time progress monitoring and cost tracking
- 🗂️ Clean output structure: converted/, metadata/, temp/
- 🔧 Automatic markdown linting and formatting
- 🧹 Smart cleanup of temporary files and old sessions

- **Utility Commands:**
```bash
python src/batch/auto_batch.py --list-recent # Show recent conversions
python src/batch/auto_batch.py --summary # Daily cost summary
python src/batch/auto_batch.py --cleanup # Manual cleanup
```
- **Local Linting (Zero API Cost):**
```bash
# Lint all converted files

python quick_lint.py outputs/converted

# Lint single file

python quick_lint.py myfile.md
```
See the [Auto Batch Guide](docs/guides/AUTO_BATCH_GUIDE.md) for complete documentation.

### Single File Processing

**Using the SSOT Configuration System:**
```bash
# Configuration is automatically loaded from .env file
# No need to manually set environment variables!

# PDF to markdown
python src/scripts/main.py < tests/input.pdf > output.md

# Image to markdown  
python src/scripts/main.py < input_image.png > output.md
```

**Legacy Method (not recommended):**
```bash
# Manual environment variable setup (use SSOT instead)
export OPENAI_API_KEY="your-api-key"
export OPENAI_API_BASE="your-api-base" 
export OPENAI_DEFAULT_MODEL="your-model"

python src/scripts/main.py < tests/input.pdf > output.md
```
## Advanced Usage

```bash
python src/scripts/main.py page_start page_end < tests/input.pdf > output.md
```

## Docker Usage

```bash
# Build local Docker image first
docker build -t markpdfdown .

# Using SSOT configuration (mount .env file)
docker run -i -v $(pwd)/.env:/app/.env markpdfdown < input.pdf > output.md

# Legacy method (manual environment variables)
docker run -i -e OPENAI_API_KEY=your-api-key -e OPENAI_API_BASE=your-api-base -e OPENAI_DEFAULT_MODEL=your-model markpdfdown < input.pdf > output.md
```
## Development Setup

### Code Quality Tools

This project uses `ruff` for linting and formatting, and `pre-commit` for automated code quality checks.

### Install development dependencies

```bash
# If using uv
uv sync --group dev

# If using pip
pip install -e ".[dev]"
```

### Set up pre-commit hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit on all files (optional)
pre-commit run --all-files
```

### Code formatting and linting

```bash
# Format code with ruff
ruff format

# Run linting checks
ruff check

# Fix auto-fixable issues
ruff check --fix
```
## Requirements

- Python 3.9+
- [uv](https://astral.sh/uv/) (recommended for package management) or conda/pip
- Dependencies specified in `pyproject.toml`
- Access to the specified multimodal AI model

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch ( `git checkout -b feature/amazing-feature` )
3. Set up the development environment:
 `bash
 uv sync --group dev
 pre-commit install
 `
4. Make your changes and ensure code quality:
 `bash
 ruff format
 ruff check --fix
 pre-commit run --all-files
 `
5. Commit your changes ( `git commit -m 'feat: Add some amazing feature'` )
6. Push to the branch ( `git push origin feature/amazing-feature` )
7. Open a Pull Request

Please ensure your code follows the project's coding standards by running the linting and formatting tools before submitting.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

## Attribution

This project is based on [MarkPDFDown](https://github.com/MarkPDFdown/markpdfdown) by the original MarkPDFDown team.

**Original Project:** [MarkPDFDown Repository](https://github.com/MarkPDFdown/markpdfdown)  
**Original License:** Apache License 2.0

**Enterprise Enhancements by Joseph Wright ([@ch0t4nk](https://github.com/ch0t4nk)):**
- 🔧 Single Source of Truth (SSOT) Configuration System v3.0
- 🔒 Enterprise Security Framework with API key protection and git history cleanup
- 📚 Comprehensive documentation suite for enterprise adoption
- 🛡️ Security best practices and incident response procedures
- 🎯 Centralized configuration management with .env template system
- 👥 Team collaboration features and secure onboarding procedures

## Acknowledgments

- Thanks to the developers of the multimodal AI models that power this tool
- Inspired by the need for better PDF to Markdown conversion tools
