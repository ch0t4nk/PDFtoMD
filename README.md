<div align="center">

<h1>MarkPDFDown</h1>
<p align="center">English | <a href="./README_zh.md">中文</a> </p>

[![Size]][hub_url]
[![Pulls]][hub_url]
[![Tag]][tag_url]
[![License]][license_url]
<p>A powerful tool that leverages multimodal large language models to transcribe PDF files into Markdown format.</p>![markpdfdown](https://raw.githubusercontent.com/markpdfdown/markpdfdown/refs/heads/master/tests/markpdfdown.png)

</div>

## Overview

MarkPDFDown is designed to simplify the process of converting PDF documents into clean, editable Markdown text. By utilizing advanced multimodal AI models, it can accurately extract text, preserve formatting, and handle complex document structures including tables, formulas, and diagrams.

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

## Demo![Image](https://raw.githubusercontent.com/markpdfdown/markpdfdown/refs/heads/master/tests/demo_02.png)

## Installation

### Using uv (Recommended)
`bash
# Install uv if you haven't already

curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository

git clone https://github.com/MarkPDFdown/markpdfdown.git
cd markpdfdown

# Install dependencies and create virtual environment

uv sync
`
### Using conda
`bash
conda create -n markpdfdown python=3.9
conda activate markpdfdown

# Clone the repository

git clone https://github.com/MarkPDFdown/markpdfdown.git
cd markpdfdown

# Install dependencies

pip install -e.
`
## Usage

### 🤖 Auto Batch Processing (Recommended)

For processing multiple PDFs with **50% cost savings** using OpenAI Batch API:
`bash
# Quick start - process all PDFs in examples/pdfs/ folder

python batch/auto_batch.py

# Custom folders

python batch/auto_batch.py documents outputs

# Windows users can double-click

auto_batch.bat
`
- *Batch Processing Features:**
- ✅ Fully automated workflow (set it and forget it)
- 💰 50% cost savings with OpenAI Batch API
- 📊 Real-time progress monitoring and cost tracking
- � Clean output structure: converted/, metadata/, temp/
- 🔧 Automatic markdown linting and formatting
- 🧹 Smart cleanup of temporary files and old sessions

- *Utility Commands:**
`bash
python batch/auto_batch.py --list-recent # Show recent conversions
python batch/auto_batch.py --summary # Daily cost summary
python batch/auto_batch.py --cleanup # Manual cleanup
`
- *Local Linting (Zero API Cost):**
`bash
# Lint all converted files

python quick_lint.py outputs/converted

# Lint single file

python quick_lint.py myfile.md
`
See the [Auto Batch Guide](AUTO_BATCH_GUIDE.md) for complete documentation.

### Single File Processing
`bash
# Set up your OpenAI API key

export OPENAI_API_KEY="your-api-key"

# Optionally, set up your OpenAI API base

export OPENAI_API_BASE="your-api-base"

# Optionally, set up your OpenAI API model

export OPENAI_DEFAULT_MODEL="your-model"

# pdf to markdown

python main.py < tests/input.pdf > output.md

# image to markdown

python main.py < input_image.png > output.md
`
## Advanced Usage
`bash
python main.py page_start page_end < tests/input.pdf > output.md
`
## Docker Usage
`bash
docker run -i -e OPENAI_API_KEY=your-api-key -e OPENAI_API_BASE=your-api-base -e OPENAI_DEFAULT_MODEL=your-model jorbenzhu/markpdfdown < input.pdf > output.md
`
## Development Setup

### Code Quality Tools

This project uses `ruff` for linting and formatting, and `pre-commit` for automated code quality checks.

#### Install development dependencies
`bash
# If using uv

uv sync --group dev

# If using pip

pip install -e ".[dev]"
`
#### Set up pre-commit hooks
`bash
# Install pre-commit hooks

pre-commit install

# Run pre-commit on all files (optional)

pre-commit run --all-files
`
#### Code formatting and linting
`bash
# Format code with ruff

ruff format

# Run linting checks

ruff check

# Fix auto-fixable issues

ruff check --fix
`
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

## Acknowledgments

- Thanks to the developers of the multimodal AI models that power this tool
- Inspired by the need for better PDF to Markdown conversion tools

[hub_url]: https://hub.docker.com/r/jorbenzhu/markpdfdown/
[tag_url]: https://github.com/markpdfdown/markpdfdown/releases
[license_url]: https://github.com/markpdfdown/markpdfdown/blob/main/LICENSE

[Size]: https://img.shields.io/docker/image-size/jorbenzhu/markpdfdown/latest?color=066da5&label=size
[Pulls]: https://img.shields.io/docker/pulls/jorbenzhu/markpdfdown.svg?style=flat&label=pulls&logo=docker
[Tag]: https://img.shields.io/github/release/markpdfdown/markpdfdown.svg
[License]: https://img.shields.io/github/license/markpdfdown/markpdfdown
