"""
Single PDF to Markdown Converter.

Usage: python convert_single.py <pdf_filename>
"""

import os
import subprocess
import sys
import time
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from config import config


def convert_single_pdf(pdf_filename):
    """Convert a single PDF file to Markdown."""

    # Check if file exists in pdfs directory
    pdf_path = os.path.join(str(config.DEFAULT_PDF_FOLDER), pdf_filename)
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        print("Available PDF files:")
        pdf_files = [
            f
            for f in os.listdir(str(config.DEFAULT_PDF_FOLDER))
            if f.lower().endswith(".pdf")
        ]
        for f in sorted(pdf_files):
            print(f"   - {f}")
        return False

    # Prepare output
    pdf_name = Path(pdf_filename).stem
    output_dir = str(config.DEFAULT_CONVERTED_FOLDER)
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{pdf_name}.md")

    print(f"🔄 Converting: {pdf_filename}")
    print(f"📄 Input: {pdf_path}")
    print(f"📝 Output: {output_file}")
    print("-" * 40)

    try:
        # Use PowerShell to pipe the PDF content to main.py
        cmd = [
            "powershell",
            "-Command",
            f'Get-Content "{pdf_path}" -Encoding Byte -Raw | '
            f'C:/Python313/python.exe src/core/main.py > "{output_file}"',
        ]

        start_time = time.time()
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.getcwd(), check=False
        )
        end_time = time.time()

        if result.returncode == 0:
            file_size = (
                os.path.getsize(output_file) if os.path.exists(output_file) else 0
            )
            print("✅ Conversion successful!")
            print(f"   ⏱️  Time: {end_time - start_time:.1f} seconds")
            print(f"   📊 Output size: {file_size:,} bytes")
            print(f"   📁 Saved to: {output_file}")
            return True
        else:
            print("❌ Conversion failed!")
            if result.stderr:
                print(f"   Error: {result.stderr}")
            return False

    except (subprocess.SubprocessError, OSError) as e:
        print(f"❌ Exception during conversion: {e}")
        return False


def main():
    """Main function for command-line usage."""
    if len(sys.argv) != 2:
        print("Usage: python convert_single.py <pdf_filename>")
        print("\nAvailable PDF files:")
        if os.path.exists(str(config.DEFAULT_PDF_FOLDER)):
            pdf_files = [
                f
                for f in os.listdir(str(config.DEFAULT_PDF_FOLDER))
                if f.lower().endswith(".pdf")
            ]
            for f in sorted(pdf_files):
                print(f"   - {f}")
        else:
            print("   No pdfs/ directory found!")
        return

    pdf_filename = sys.argv[1]
    convert_single_pdf(pdf_filename)


if __name__ == "__main__":
    main()
