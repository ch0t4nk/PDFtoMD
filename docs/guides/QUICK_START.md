# 🚀 Quick Start Guide - Auto Batch Processing

## TL;DR - 30 Second Setup

1. **Configure API Key**: 
   ```bash
   # Copy template and edit with your API key
   cp .env.template .env
   # Edit .env: OPENAI_API_KEY="sk-your-key"
   ```
2. **Test Configuration**: `python config.py`
3. **Add PDFs**: Put your PDFs in the `pdfs/` folder
4. **Run**: `python src/batch/auto_batch.py` (or double-click `auto_batch_launcher.bat` on Windows)
5. **Wait**: Processing happens automatically with progress updates
6. **Done**: Results in `outputs/converted/session_YYYYMMDD_HHMMSS/`

**That's it!** ✨ You get 50% cost savings, automated monitoring, and organized outputs.

---

## What Happens Automatically

```
🤖 AUTO BATCH PROCESSING
├── 🔍 Scan for PDFs (finds all .pdf files)
├── 📊 Estimate costs (shows before processing)
├── 🚀 Submit to OpenAI Batch API (50% cheaper)
├── ⏰ Monitor progress (automatic status checks)
├── 📥 Download results (all files converted)
├── 💰 Analyze costs (detailed breakdown)
├── 📁 Organize outputs (timestamped folders)
└── 🧹 Cleanup (removes temporary files)
```

## Example Run

```bash
$ python auto_batch.py
🚀 AUTOMATED BATCH PDF PROCESSING
📁 Input Folder: pdfs
📁 Output Folder: converted_markdown
🆔 Session ID: 20250715_202045

⏰ Step 1: Scanning for PDFs in pdfs
✅ Found 7 PDF files (3.0 MB total)

⏰ Step 2: Setting up workspace
✅ Workspace ready: converted_markdown\session_20250715_202045

⏰ Step 3: Estimating processing costs
📊 Estimated Cost: ~$0.47 (93 pages)

⏰ Step 4: Submitting batch to OpenAI
✅ Batch submitted: batch_6876f077... (93 requests)

⏰ Step 5: Monitoring batch
🔄 Check #1: validating (0/93 - 0.0%)
🔄 Check #4: in_progress (49/93 - 52.7%)
🔄 Check #7: completed (93/93 - 100.0%)
✅ Batch completed in 3.0 minutes!

⏰ Step 6: Retrieving results
✅ Created 7 markdown files

⏰ Step 7: Analyzing costs
💰 Total Cost: $0.4676 ($0.005/page)

⏰ Step 8: Organizing outputs
✅ Session organized: converted_markdown\session_20250715_202045

🎉 PROCESSING COMPLETE!
📁 Results: converted_markdown\session_20250715_202045
```

## Cost Savings Example

| Method | Cost per Page | 100 Pages | 1000 Pages |
|--------|---------------|-----------|------------|
| Standard API | ~$0.010 | $1.00 | $10.00 |
| **Batch API** | **~$0.005** | **$0.50** | **$5.00** |
| **Savings** | **50%** | **$0.50** | **$5.00** |

## Output Structure

```
outputs/
├── converted/
│   └── session_20250715_202045/
│       ├── document1_batch.md
│       ├── document2_batch.md
│       └── document3_batch.md
├── metadata/
│   └── 20250715_summary.json
└── temp/ (automatically cleaned up)
```

## Configuration (Optional)

All settings are managed through the SSOT configuration system in `config.py`:

```python
# Configuration is automatically loaded from .env
# To customize, edit .env file:

# API Configuration
OPENAI_API_KEY="sk-your-key"
OPENAI_API_BASE="https://api.openai.com/v1" 
OPENAI_DEFAULT_MODEL="gpt-4o-mini"

# Directory Settings  
PDF_FOLDER="pdfs"
OUTPUT_FOLDER="outputs"
TEMP_FOLDER="temp"

# Processing Settings
TEMPERATURE=0.05
MAX_TOKENS=8192

# Cost Controls
COST_WARNING_THRESHOLD=1.0
COST_ALERT_THRESHOLD=5.0
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "No PDFs found" | Put PDFs in `pdfs/` folder |
| "API key not set" | Run `python config.py` to check, edit `.env` file |
| "Configuration error" | Copy `.env.template` to `.env` and configure |
| "Insufficient quota" | Check OpenAI billing dashboard |
| "Batch failed" | Check internet connection, try again |

## Next Steps

- 📖 Read the [SSOT Configuration Guide](SSOT_GUIDE.md) for detailed setup
- 📖 Read the [complete batch guide](AUTO_BATCH_GUIDE.md) for advanced features  
- ⚙️ Customize settings in `.env` file
- 📊 Check cost analysis in the outputs/metadata/ folder
- 🔄 Run `python monitor_batch.py batch_id` for live monitoring

---

**Happy batch processing!** 🚀 For questions, see the [main README](../../README.md) or [detailed guide](AUTO_BATCH_GUIDE.md).
