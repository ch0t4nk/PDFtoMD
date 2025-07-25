# PDFtoMD Installation Guide

## 🚀 Quick Start Installation

### Prerequisites

- Python 3.8 or higher
- Git (for cloning repository)
- Virtual environment (recommended)

### Method 1: Git Clone (Recommended)

`bash

# Clone the repository

git clone https://github.com/ch0t4nk/PDFtoMD.git
cd PDFtoMD

# Create virtual environment (recommended)

python -m venv PDFtoMD-env

# Activate virtual environment

# On Windows:

PDFtoMD-env\Scripts\activate

# On macOS/Linux:

source PDFtoMD-env/bin/activate

# Install dependencies

pip install -r requirements.txt

# Verify installation

python test_comprehensive.py
`

### Method 2: Download Release Archive

1. Download the latest release from [GitHub Releases](https://github.com/ch0t4nk/PDFtoMD/releases)
2. Extract the archive to your desired location
3. Follow the same virtual environment and dependency installation steps above

## 🔧 Configuration

### Basic Setup

1. Copy the sample configuration:
 `bash
 cp config/auto_batch_config_sample.py config/auto_batch_config.py
 `
2. Edit configuration with your preferences:
 `bash
 # Edit config/auto_batch_config.py
 # Add your OpenAI API key and customize settings
 `

### Environment Variables

Create a `.env` file in the project root:
`env
OPENAI_API_KEY=your_api_key_here
`

## 🎯 Usage Examples

### Basic PDF Conversion

`bash
python launcher.py path/to/your/document.pdf
`

### Batch Processing

`bash
python launcher.py --batch path/to/pdf/directory/
`

### Auto-batch with Configuration

`bash
python auto_batch_launcher.bat
`

## 🧪 Verification

Run the comprehensive test suite to verify your installation:
`bash
python test_comprehensive.py
`
Expected output: `✅ All 11 comprehensive tests passed!`

## 🔒 Security Notes

- All dependencies are pinned to secure versions
- GitHub Dependabot vulnerabilities resolved in v4.1.0
- Regular security updates recommended

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure virtual environment is activated and dependencies installed
2. **API Key Issues**: Verify `.env` file configuration
3. **Permission Errors**: Check file permissions for input/output directories

### Getting Help

- Check the [documentation](docs/)
- Review [examples](examples/)
- Open an issue on GitHub for bugs or feature requests

## 📝 Development Installation

For contributing to the project:
`bash

# Install development dependencies

pip install -r requirements-dev.txt

# Run linting

ruff check.
ruff format.

# Run tests

python test_comprehensive.py
`

## 🔄 Updating

To update to the latest version:
`bash
git pull origin master
pip install -r requirements.txt --upgrade
`
- --

- *Need help?** Open an issue on [GitHub](https://github.com/ch0t4nk/PDFtoMD/issues)\n
