# 🚀 Quick Start Guide - Auto Batch Processing

## TL;DR - 30 Second Setup

1. **Set API Key**: `export OPENAI_API_KEY="sk-your-key"`
2. **Add PDFs**: Put your PDFs in the `pdfs/` folder
3. **Run**: `python auto_batch.py` (or double-click `auto_batch.bat` on Windows)
4. **Wait**: Processing happens automatically with progress updates
5. **Done**: Results in `converted_markdown/session_YYYYMMDD_HHMMSS/`

- *That's it!** ✨ You get 50% cost savings, automated monitoring, and organized outputs.

- --

## What Happens Automatically
`
🤖 AUTO BATCH PROCESSING
├── 🔍 Scan for PDFs (finds all.pdf files)
├── 📊 Estimate costs (shows before processing)
├── 🚀 Submit to OpenAI Batch API (50% cheaper)
├── ⏰ Monitor progress (automatic status checks)
├── 📥 Download results (all files converted)
├── 💰 Analyze costs (detailed breakdown)
├── 📁 Organize outputs (timestamped folders)
└── 🧹 Cleanup (removes temporary files)
`
## Example Run
`bash
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
`
## Cost Savings Example

| Method | Cost per Page | 100 Pages | 1000 Pages |
|---|---|---|---|
| Standard API | ~$0.010 | $1.00 | $10.00 |
| **Batch API** | **~$0.005** | **$0.50** | **$5.00** |
| **Savings** | **50%** | **$0.50** | **$5.00** |

## Output Structure
`
converted_markdown/
└── session_20250715_202045/
 ├── markdown_files/
 │ ├── document1_batch.md
 │ ├── document2_batch.md
 │ └── document3_batch.md
 ├── cost_analysis.json
 └── README.md (session summary)
`
## Configuration (Optional)

Create `auto_batch_config.py` for customization:
`python
# Basic settings

DEFAULT_PDF_FOLDER = "my_pdfs" # Input folder
DEFAULT_OUTPUT_FOLDER = "converted" # Output folder

# Quality settings

TEMPERATURE = 0.05 # 0.0 = consistent, 1.0 = creative
MAX_TOKENS = 8192 # Output length per page

# Cost controls

COST_WARNING_THRESHOLD = 1.00 # Warn if cost > $1.00
COST_ALERT_THRESHOLD = 5.00 # Alert if cost > $5.00
`
## Troubleshooting

| Problem | Solution |
|---|---|
| "No PDFs found" | Put PDFs in `pdfs/` folder |
| "API key not set" | `export OPENAI_API_KEY="sk-..."` |
| "Insufficient quota" | Check OpenAI billing dashboard |
| "Batch failed" | Check internet connection, try again |

## Next Steps

- 📖 Read the [complete guide](AUTO_BATCH_GUIDE.md) for advanced features
- ⚙️ Customize settings in `auto_batch_config.py`
- 📊 Check cost analysis in the session folder
- 🔄 Run `python monitor_batch.py batch_id` for live monitoring

- --

- *Happy batch processing!** 🚀 For questions, see the [main README](README.md) or [detailed guide](AUTO_BATCH_GUIDE.md).
