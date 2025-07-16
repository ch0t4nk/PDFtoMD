# 🔧 Single Source of Truth (SSOT) Configuration System

## 🎯 Overview

MarkPDFDown now uses a centralized configuration system that provides a **Single Source of Truth** for all settings, API keys, and directory paths. This eliminates hardcoded values scattered throughout the codebase and provides secure, centralized configuration management.

## 🔑 Key Benefits

✅ **Centralized API Key Management** - All API keys managed from one location  
✅ **Security First** - API keys never hardcoded in source files  
✅ **Environment Flexibility** - Easy switching between development/production  
✅ **Default Directory Management** - Consistent paths across all tools  
✅ **Feature Flags** - Enable/disable features globally  
✅ **Cost Management** - Centralized thresholds and monitoring  

## 📁 File Structure

```
markpdfdown/
├── config.py              # 🎯 SSOT Configuration System
├── .env                    # 🔒 Environment Variables (DO NOT COMMIT)
├── .env.template          # 📋 Template for .env file
├── .env.backup            # 💾 Your original .env (with API key)
└── migrate_to_ssot.py     # 🚀 Migration tool
```

## 🚀 Quick Setup

### 1. Configure Your API Key

**SECURE SETUP (Recommended):**
```bash
# Copy the template to create your .env file
cp .env.template .env

# Edit .env file and add your OpenAI API key
# OPENAI_API_KEY="sk-your-actual-api-key-here"
```

**Alternative Setup:**
```bash
# Direct edit of .env file
echo 'OPENAI_API_KEY="sk-your-actual-api-key-here"' > .env
```

### 2. Test Configuration

```bash
python config.py
```

**Expected Output:**
```
🔧 MarkPDFDown Configuration Summary
==================================================
📁 PDF Folder: C:\Users\...\markpdfdown\pdfs
📁 Output Folder: C:\Users\...\markpdfdown\outputs
📁 Temp Folder: C:\Users\...\markpdfdown\temp
🤖 Model: gpt-4o-mini
🌡️  Temperature: 0.05
🔢 Max Tokens: 8192
💰 Cost Warning: $1.0
🚨 Cost Alert: $5.0
🔑 API Key: ✅ Configured
🌐 API Base: https://api.openai.com/v1
==================================================
✅ Configuration test complete!
```

### 3. You're Ready!

All tools now automatically use the SSOT configuration. No more manual environment variable setup!
🌡️  Temperature: 0.05
🔢 Max Tokens: 8192
💰 Cost Warning: $1.0
🚨 Cost Alert: $5.0
🔑 API Key: ✅ Configured
🌐 API Base: https://api.openai.com/v1
==================================================
```

### 3. Test Your Application

```bash
# Test with the launcher
python launcher.py auto-batch --help

# Or test individual components
python src/scripts/auto_batch.py --help
```

## 🔧 Configuration Options

### API Configuration

| Setting | Environment Variable | Default | Description |
|---------|---------------------|---------|-------------|
| API Key | `OPENAI_API_KEY` | **Required** | Your OpenAI API key |
| API Base | `OPENAI_API_BASE` | `https://api.openai.com/v1` | API endpoint |
| Model | `OPENAI_DEFAULT_MODEL` | `gpt-4o-mini` | Default AI model |

### Directory Configuration

| Setting | Environment Variable | Default | Description |
|---------|---------------------|---------|-------------|
| PDF Folder | `DEFAULT_PDF_FOLDER` | `pdfs` | Input PDF files |
| Output Folder | `DEFAULT_OUTPUT_FOLDER` | `outputs` | All generated files |
| Temp Folder | `DEFAULT_TEMP_FOLDER` | `temp` | Temporary files |

### Processing Configuration

| Setting | Environment Variable | Default | Description |
|---------|---------------------|---------|-------------|
| Temperature | `TEMPERATURE` | `0.05` | AI creativity (0.0-1.0) |
| Max Tokens | `MAX_TOKENS` | `8192` | Response length |
| DPI | `DPI` | `200` | Image extraction quality |

### Cost Management

| Setting | Environment Variable | Default | Description |
|---------|---------------------|---------|-------------|
| Warning Threshold | `COST_WARNING_THRESHOLD` | `1.00` | Warning at $1.00 |
| Alert Threshold | `COST_ALERT_THRESHOLD` | `5.00` | Alert at $5.00 |

## 🔄 Using the Configuration in Code

### Basic Usage

```python
from config import config

# API Configuration
client = OpenAI(
    api_key=config.OPENAI_API_KEY,
    base_url=config.OPENAI_API_BASE
)

# Directory Paths
pdf_folder = config.DEFAULT_PDF_FOLDER
output_folder = config.DEFAULT_CONVERTED_FOLDER

# Processing Settings
temperature = config.TEMPERATURE
max_tokens = config.MAX_TOKENS
```

### Advanced Usage

```python
from config import config, get_openai_client_config, ensure_directories

# Ensure directories exist
ensure_directories()

# Get OpenAI client configuration
client_config = get_openai_client_config()
client = OpenAI(**client_config)

# Get model configuration
model_config = get_model_config()
response = client.chat.completions.create(**model_config, messages=[...])

# Check cost thresholds
if estimated_cost > config.COST_WARNING_THRESHOLD:
    print(f"⚠️ Cost warning: ${estimated_cost}")
```

## 🔒 Security Features

### ✅ What's Secure Now

- ✅ **No API keys in source code** - All keys in `.env` file
- ✅ **`.env` in .gitignore** - Never committed to git
- ✅ **Template system** - `.env.template` for sharing configuration structure
- ✅ **Backup system** - Original `.env` saved to `.env.backup`

### 🚨 Security Best Practices

1. **Never commit `.env`** - It contains your actual API key
2. **Use `.env.template`** - For sharing configuration structure
3. **Rotate API keys regularly** - Update in `.env` file only
4. **Set environment permissions** - Restrict `.env` file access

## 🌍 Environment Switching

### Development vs Production

Create different `.env` files:
```bash
# Development
cp .env .env.development

# Production  
cp .env .env.production

# Switch environments
cp .env.development .env  # Use development
cp .env.production .env   # Use production
```

### LM Studio (Local) Setup

Update `.env` for local LM Studio:
```bash
OPENAI_API_KEY="lm-studio"
OPENAI_API_BASE="http://192.168.56.1:1234/v1"
OPENAI_DEFAULT_MODEL="Qwen2-VL-7B-Instruct"
```

## 📊 Migration Summary

The SSOT migration updated **35 files** with **193 changes**:

### ✅ Changes Made

- **Added config imports** to all Python files
- **Replaced `os.getenv()`** calls with `config.PROPERTY`
- **Replaced hardcoded paths** with `config.DEFAULT_FOLDER`
- **Removed duplicate `load_dotenv()`** calls
- **Created backup files** for all modified files

### 📁 Files Updated

- **Core modules**: `main.py`, `main_fast.py`
- **Batch processing**: `auto_batch.py`, `batch_api.py`, `master.py`
- **Conversion tools**: All tools in `tools/conversion/`
- **Testing utilities**: All files in `tools/testing/`
- **Utils**: All utility modules

## 🔄 Rollback Instructions

If you need to rollback the SSOT migration:

```bash
# Restore from backups
find . -name "*.backup" -exec bash -c 'mv "$1" "${1%.backup}"' _ {} \;

# Or selectively restore specific files
mv src/batch/batch_api.py.backup src/batch/batch_api.py
```

## 🆘 Troubleshooting

### "OPENAI_API_KEY not found"

1. Check your `.env` file exists
2. Verify API key is set: `OPENAI_API_KEY="sk-..."`
3. Test configuration: `python config.py`

### Import Errors

1. Ensure you're running from project root
2. Check `config.py` is in root directory
3. Verify Python path includes current directory

### Path Issues

1. All paths are now relative to project root
2. Use `config.DEFAULT_PDF_FOLDER` instead of `"pdfs"`
3. Use `str(config.DEFAULT_PDF_FOLDER)` for string operations

## 📋 Next Steps

1. ✅ **Test your API key** - Run `python config.py`
2. ✅ **Test your application** - Run `python launcher.py auto-batch --help`
3. ✅ **Customize settings** - Edit `.env` file as needed
4. ✅ **Clean up backups** - Remove `.backup` files when satisfied
5. ✅ **Update documentation** - Reflect new configuration system

---

🎉 **Congratulations!** Your MarkPDFDown application now uses a secure, centralized configuration system with your API keys safely managed outside of source code.
