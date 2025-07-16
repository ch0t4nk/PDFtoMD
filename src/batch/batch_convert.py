# Batch PDF to Markdown Converter - OPTIMIZED VERSION
# Uses convert_fast.py with OpenAI GPT-4o-mini for high-quality conversion

import os
import subprocess
import time
import sys
from pathlib import Path
import importlib.util

# Import config using relative path
current_dir = Path(__file__).parent
root_dir = current_dir.parent.parent
config_path = root_dir / "config.py"

if config_path.exists():
    spec = importlib.util.spec_from_file_location("config", config_path)
    if spec and spec.loader:
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        config = config_module.config
    else:
        raise ImportError("Failed to load config spec")
else:
    raise ImportError("Config file not found")

def get_converted_files():
    """Get list of already converted files to avoid re-processing."""
    converted_dir = Path(str(config.DEFAULT_CONVERTED_FOLDER))
    if not converted_dir.exists():
        return []

    converted_files = list(converted_dir.glob("*_fast.md"))
    # Extract original PDF names from converted filenames
    converted_pdfs = []
    for md_file in converted_files:
        # Remove _fast.md suffix to get original PDF name
        pdf_name = md_file.stem.replace("_fast", "") + ".pdf"
        converted_pdfs.append(pdf_name)

    return converted_pdfs

def convert_pdf_to_markdown(pdf_file):
    """Convert a single PDF to Markdown using convert_fast.py"""

    print(f"🚀 Converting: {pdf_file}")
    print("=" * 60)

    try:
        start_time = time.time()

        # Use the optimized convert_fast.py script
        result = subprocess.run([
            sys.executable, "convert_fast.py", pdf_file
        ], capture_output=True, text=True, cwd=os.getcwd())

        end_time = time.time()
        duration = end_time - start_time

        if result.returncode == 0:
            print(f"✅ Success! Completed in {duration:.1f} seconds")
            return True
        else:
            print(f"❌ Failed with return code {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return False

def main():
    """Main batch processing function."""
    print("🔄 PDF Batch Converter - OPTIMIZED")
    print("=" * 60)
    print("📁 Using OpenAI GPT-4o-mini for high-quality conversion")
    print("⚡ Fast conversion settings enabled")
    print()

    # Directories
    pdf_dir = Path(str(config.DEFAULT_PDF_FOLDER))
    output_dir = Path(str(config.DEFAULT_CONVERTED_FOLDER))

    # Ensure directories exist
    if not pdf_dir.exists():
        print("❌ PDFs directory not found!")
        return

    output_dir.mkdir(exist_ok=True)

    # Find all PDF files
    pdf_files = [f.name for f in pdf_dir.glob("*.pdf")]

    if not pdf_files:
        print("❌ No PDF files found in pdfs/ directory")
        return

    # Get already converted files
    converted_files = get_converted_files()

    # Filter out already converted files
    pending_files = [pdf for pdf in pdf_files if pdf not in converted_files]

    print(f"📊 Found {len(pdf_files)} total PDF files")
    print(f"✅ Already converted: {len(converted_files)} files")
    print(f"⏳ Pending conversion: {len(pending_files)} files")

    if converted_files:
        print(f"\n📋 Already converted:")
        for pdf in converted_files:
            print(f"   ✓ {pdf}")

    if not pending_files:
        print("\n🎉 All PDF files have already been converted!")
        return

    print(f"\n� Files to convert:")
    for i, pdf in enumerate(pending_files, 1):
        print(f"   {i}. {pdf}")

    print(f"\n🚀 Starting batch conversion of {len(pending_files)} files...")

    successful = 0
    failed = 0
    total_start_time = time.time()

    for i, pdf_file in enumerate(pending_files, 1):
        print(f"\n📄 Processing {i}/{len(pending_files)}: {pdf_file}")

        if convert_pdf_to_markdown(pdf_file):
            successful += 1
        else:
            failed += 1

        # Add a delay between conversions for OpenAI rate limiting
        if i < len(pending_files):
            print("⏳ Waiting 10 seconds before next conversion (OpenAI rate limiting)...")
            time.sleep(10)

    total_end_time = time.time()
    total_duration = total_end_time - total_start_time

    print("\n" + "=" * 60)
    print("📊 BATCH CONVERSION SUMMARY")
    print("=" * 60)
    print(f"✅ Successful: {successful} files")
    print(f"❌ Failed: {failed} files")
    print(f"⏱️  Total time: {total_duration:.1f} seconds")
    if successful > 0:
        print(f"� Average time per file: {total_duration/len(pending_files):.1f} seconds")
    print()

    if successful > 0:
        print("🎉 Batch conversion completed!")
        print("📁 Check the 'converted/' directory for your markdown files")

    if failed > 0:
        print("⚠️  Some conversions failed. Check the error messages above.")

if __name__ == "__main__":
    main()