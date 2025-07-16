# 🤖 Auto Batch Processing Guide

## Quick Start

The easiest way to convert multiple PDFs to Markdown using the OpenAI Batch API with **50% cost savings**:

### Windows Users
Double-click `auto_batch.bat` or run:
```cmd
auto_batch.bat
```

### All Platforms
```bash
python batch/auto_batch.py
```

That's it! The system will automatically:
- 🔍 Find all PDFs in the `examples/pdfs` folder
- 📊 Estimate costs
- 🚀 Submit to OpenAI Batch API
- ⏰ Monitor progress
- 📥 Download results
- 📁 Organize outputs in clean structure
- 🔧 Auto-lint for better formatting
- 🧹 Clean up temporary files

## Table of Contents

- [Features](#features)
- [Installation & Setup](#installation--setup)
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [Linting System](#linting-system)
- [Configuration](#configuration)
- [Cost Management](#cost-management)
- [Output Structure](#output-structure)
- [Troubleshooting](#troubleshooting)
- [API Reference](#api-reference)

## Features

### 🎯 **Fully Automated Workflow**
- **Zero interaction required** - Set it and forget it
- **Smart progress monitoring** - Automatic status checks
- **Intelligent cost estimation** - Know costs before processing
- **Clean output organization** - All files in outputs/converted/

### 💰 **Cost Optimization**
- **50% savings** with OpenAI Batch API vs standard API
- **Detailed cost tracking** - Per-page and per-document analysis
- **Smart batching** - Optimal request grouping

### 🔧 **Local Linting System**
- **Zero API cost** - Local formatting improvements
- **Automatic cleanup** - PDF artifacts and formatting issues
- **Significant optimization** - 30-40% file size reduction
- **Cost alerts** - Configurable spending thresholds

### 🔄 **Robust Processing**
- **Automatic retries** - Handles temporary failures
- **Progress persistence** - Resume interrupted batches
- **Quality enhancement** - Advanced prompting for better output
- **Comprehensive logging** - Full audit trail

### 📊 **Advanced Analytics**
- **Usage statistics** - Detailed consumption reports
- **Performance metrics** - Processing speed and efficiency
- **Cost comparison** - Batch vs standard API savings
- **Quality assessment** - Token efficiency analysis

## Installation & Setup

### Prerequisites
- Python 3.9+
- OpenAI API key with billing enabled
- 2GB+ available disk space (for temporary files)

### 1. Environment Setup
```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# Windows PowerShell:
$env:OPENAI_API_KEY="your-api-key-here"

# Windows Command Prompt:
set OPENAI_API_KEY=your-api-key-here
```

### 2. Verify Installation
```bash
python auto_batch.py --help
```

Should display the usage information and confirm everything is working.

## Basic Usage

### Default Processing
Process all PDFs in the `pdfs` folder:
```bash
python auto_batch.py
```

### Custom Input Folder
```bash
python auto_batch.py documents
```

### Custom Input and Output
```bash
python auto_batch.py documents converted_docs
```

### Example Complete Workflow
```bash
# 1. Put your PDFs in the pdfs folder
cp *.pdf pdfs/

# 2. Run the auto batch processor
python auto_batch.py

# 3. Wait for completion (will show progress)
# Results will be in: converted_markdown/session_YYYYMMDD_HHMMSS/
```

## Advanced Usage

### Batch File Processing (Windows)
For convenience, use the Windows batch file:
```cmd
auto_batch.bat
```

This automatically handles:
- Directory navigation
- Error handling
- Window persistence (so you can see results)

### Custom Configuration
Create `auto_batch_config.py` from the sample:
```bash
cp auto_batch_config_sample.py auto_batch_config.py
```

Edit the configuration:
```python
# auto_batch_config.py
DEFAULT_PDF_FOLDER = "my_documents"
DEFAULT_OUTPUT_FOLDER = "my_converted"
TEMPERATURE = 0.05  # Consistency vs creativity
MAX_TOKENS = 8192   # Output length
COST_WARNING_THRESHOLD = 2.00  # Alert at $2.00
```

### Processing Specific File Types
```bash
# Process only files matching pattern
python auto_batch.py --pattern "*.pdf"

# Skip certain files
python auto_batch.py --exclude "draft_*.pdf"
```

### Monitoring Long-Running Batches
```bash
# Check status of running batch
python monitor_batch.py batch_12345...

# Track costs in real-time
python track_batch_cost.py batch_12345...
```

### Utility Commands
```bash
# Show recent conversions
python batch/auto_batch.py --list-recent

# Daily cost summary
python batch/auto_batch.py --summary

# Manual cleanup
python batch/auto_batch.py --cleanup
```

## Linting System

### Local Markdown Linting (Zero API Cost)

The system includes a powerful local linting engine that improves markdown formatting without any API costs:

### Automatic Linting
- **Built-in to batch processing** - Applied automatically after conversion
- **No additional cost** - Runs locally on your machine
- **Significant improvements** - 30-40% file size reduction typical

### Manual Linting
```bash
# Lint all converted files
python quick_lint.py outputs/converted

# Lint single file
python quick_lint.py myfile.md

# Lint with custom pattern
python utils/linting/markdown_linter.py outputs/converted --pattern "*.md"
```

### Linting Features
- **Excessive newlines** → Clean spacing (3+ newlines → 2)
- **Header spacing** → Proper blank lines around headers
- **Table formatting** → Clean table structure and alignment
- **List formatting** → Consistent bullet points and numbering
- **Code blocks** → Proper fencing and formatting
- **Image alt text** → Improved accessibility
- **PDF artifacts** → Remove page numbers, weird spacing
- **Whitespace cleanup** → Trailing spaces, mixed tabs/spaces
- **Section numbering** → Clean header formatting

### Linting Results Example
```
📊 Linting Results: 453KB → 277KB (39% reduction, 177KB saved)
Files processed: 4 PDF conversions
Total fixes applied: 22 formatting improvements
```

## Configuration

### Configuration File Options

Create `auto_batch_config.py` with these options:

```python
# Folder Settings
DEFAULT_PDF_FOLDER = "pdfs"           # Input folder
DEFAULT_OUTPUT_FOLDER = "converted"   # Output base folder

# Processing Quality
TEMPERATURE = 0.05      # 0.0 = deterministic, 1.0 = creative
MAX_TOKENS = 8192       # Maximum output per request
DPI = 200              # Image extraction quality

# Monitoring
CHECK_INTERVAL = 30     # Seconds between status checks
MAX_WAIT_TIME = 3600   # Max wait time (1 hour)

# Cost Management
COST_WARNING_THRESHOLD = 1.00   # Warn at $1.00
COST_ALERT_THRESHOLD = 5.00     # Alert at $5.00

# Organization
CREATE_SESSION_FOLDERS = True    # Use timestamped folders
INCLUDE_MASTER_DOCUMENT = True   # Create combined document
DETAILED_COST_REPORTS = True     # Generate cost analysis
```

### Environment Variables
```bash
# Required
OPENAI_API_KEY="sk-..."

# Optional
OPENAI_API_BASE="https://api.openai.com/v1"  # Custom endpoint
OPENAI_DEFAULT_MODEL="gpt-4o-mini"           # Default model
```

## Cost Management

### Understanding Costs

The Batch API provides **50% savings** over standard API:
- **Standard API**: ~$0.010 per page
- **Batch API**: ~$0.005 per page
- **Typical document**: $0.50-2.00 depending on complexity

### Cost Estimation
Before processing, you'll see:
```
📊 Processing Estimates:
   📄 Files: 7
   📦 Total Size: 3.0 MB
   📃 Estimated Pages: ~93
   🔢 Estimated Tokens: ~280,000
   💰 Estimated Cost: ~$0.47
   ⏱️  Estimated Time: 5-15 minutes
```

### Cost Tracking
After processing:
```
📊 COST ANALYSIS SUMMARY
==================================================
💰 Estimated Cost: $0.47
💰 Actual Cost: $0.47
💰 Difference: $+0.00 (+0.0%)
📄 Pages Processed: 93
🔢 Tokens Used: 2,890,166
⚡ Cost per Page: $0.0050
==================================================
```

### Setting Cost Limits
In your config:
```python
COST_WARNING_THRESHOLD = 1.00   # Warn before processing
COST_ALERT_THRESHOLD = 5.00     # Require confirmation
```

## Output Structure

### Clean Organized Structure (New)
```
outputs/
├── converted/           📝 All .md files with date prefixes
│   ├── 20250716_document1_batch.md
│   ├── 20250716_document2_batch.md
│   └── 20250716_document3_batch.md
├── metadata/           📊 Daily summaries and cost data
│   ├── 20250716_summary.json
│   └── 20250715_summary.json
└── temp/               🗂️ Auto-cleaned temp files (24hr lifecycle)
```

### File Naming Convention
- **Input**: `document.pdf`
- **Output**: `20250716_document_batch.md` (date prefixed)
- **Metadata**: `20250716_summary.json` (daily aggregated)

### Daily Summary JSON
```json
{
  "date": "20250716",
  "total_cost": 1.1130,
  "total_files": 4,
  "total_pages": 189,
  "average_cost_per_page": 0.0059,
  "daily_totals": {
    "total_cost": 1.1130,
    "total_files": 4,
    "total_pages": 189,
    "average_cost_per_page": 0.0059
  },
  "files": [
    {
      "filename": "document.pdf",
      "output_file": "20250716_document_batch.md",
      "pages": 16,
      "cost": 0.0777,
      "tokens": 438572,
      "cost_per_page": 0.0049,
      "timestamp": "2025-07-16T12:55:24"
    }
  ]
}
```

### Benefits of New Structure
- **📁 Easy access** - All converted files in one place
- **📅 Date organization** - Files sorted by conversion date
- **🧹 Auto cleanup** - Old temp files automatically removed
- **📊 Daily summaries** - Aggregated cost tracking
- **🔧 Auto-linted** - Files automatically formatted and optimized

## Troubleshooting

### Common Issues

#### 1. "No PDFs found"
```bash
# Check if PDFs exist
ls pdfs/*.pdf

# Create pdfs folder if missing
mkdir pdfs
cp your_documents/*.pdf pdfs/
```

#### 2. "OpenAI API key not set"
```bash
# Set the environment variable
export OPENAI_API_KEY="sk-your-key-here"

# Verify it's set
echo $OPENAI_API_KEY
```

#### 3. "Batch processing failed"
```bash
# Check batch status manually
python -c "
from batch_api import BatchPDFConverter
converter = BatchPDFConverter()
status = converter.get_batch_status('batch_12345...')
print(status)
"
```

#### 4. "Insufficient quota/credits"
- Check your OpenAI billing dashboard
- Ensure you have available credits
- Batch API requires payment method on file

### Debugging Steps

1. **Check Environment**:
   ```bash
   python -c "import os; print(os.getenv('OPENAI_API_KEY', 'NOT SET'))"
   ```

2. **Verify API Access**:
   ```bash
   python test_openai.py
   ```

3. **Check Batch Status**:
   ```bash
   python monitor_batch.py your_batch_id
   ```

4. **View Detailed Logs**:
   ```bash
   python auto_batch.py --verbose
   ```

### Performance Tips

1. **Optimize Image Quality**: 
   - Use DPI=200 for good balance
   - Higher DPI = better quality but slower processing

2. **Batch Size**:
   - 50-100 pages optimal per batch
   - Larger batches = better cost efficiency

3. **Monitoring**:
   - Check every 30 seconds for batches <100 pages
   - Check every 60 seconds for larger batches

## API Reference

### AutoBatchProcessor Class

```python
from auto_batch import AutoBatchProcessor

# Initialize
processor = AutoBatchProcessor(
    pdf_folder="documents", 
    output_folder="converted"
)

# Run complete workflow
processor.run()

# Individual steps
processor.discover_pdfs()
processor.setup_workspace()
processor.estimate_costs()
processor.submit_batch()
processor.monitor_batch()
processor.retrieve_results()
processor.analyze_costs()
processor.organize_outputs()
processor.cleanup()
```

### BatchPDFConverter Class

```python
from batch_api import BatchPDFConverter

converter = BatchPDFConverter()

# Submit batch
batch_id = converter.submit_batch(pdf_folder="pdfs")

# Monitor progress
status = converter.monitor_batch(batch_id)

# Get results
converter.download_results(batch_id, "output_folder")
```

### Master Analysis

```python
from master import PDFBatchMaster

master = PDFBatchMaster()

# Analyze usage
master.analyze_batch_usage(batch_id)

# Print summary
master.print_usage_summary()

# Cleanup old files
master.cleanup()
```

### Configuration Options

| Setting | Default | Description |
|---------|---------|-------------|
| `DEFAULT_PDF_FOLDER` | `"pdfs"` | Input folder for PDFs |
| `DEFAULT_OUTPUT_FOLDER` | `"converted_markdown"` | Output base folder |
| `TEMPERATURE` | `0.05` | AI model temperature (0.0-1.0) |
| `MAX_TOKENS` | `8192` | Maximum tokens per request |
| `DPI` | `200` | Image extraction quality |
| `CHECK_INTERVAL` | `30` | Status check interval (seconds) |
| `MAX_WAIT_TIME` | `3600` | Maximum wait time (seconds) |
| `COST_WARNING_THRESHOLD` | `1.00` | Cost warning threshold ($) |
| `COST_ALERT_THRESHOLD` | `5.00` | Cost alert threshold ($) |
| `AUTO_CLEANUP` | `True` | Auto-cleanup temporary files |
| `CREATE_SESSION_FOLDERS` | `True` | Use timestamped folders |

---

## Support

### Getting Help
- Check the [main README](README.md) for general setup
- Review [troubleshooting](#troubleshooting) section above
- Open an issue on GitHub for bugs or feature requests

### Performance Optimization
- For large batches (>1000 pages), consider splitting into smaller batches
- Use SSD storage for faster image processing
- Ensure stable internet connection for uploads/downloads

### Best Practices
1. **Start small** - Test with 1-2 PDFs first
2. **Monitor costs** - Use cost thresholds
3. **Regular cleanup** - Clean old session folders periodically
4. **Backup originals** - Keep original PDFs safe
5. **Check quality** - Review output for accuracy

---

*Happy batch processing! 🚀*
