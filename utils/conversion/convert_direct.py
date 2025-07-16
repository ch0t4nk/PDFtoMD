# Direct PDF to Markdown Converter
# This version uses Python's stdin directly instead of PowerShell

import os
import sys
import subprocess
import time
from pathlib import Path

def convert_pdf_direct(pdf_path, output_file):
    """Convert PDF directly using Python subprocess with stdin"""

    try:
        # Read the PDF file as binary
        with open(pdf_path, 'rb') as pdf_file:
            pdf_data = pdf_file.read()

        # Run main.py with the PDF data as stdin
        start_time = time.time()
        process = subprocess.Popen(
            [sys.executable, 'main.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.getcwd()
        )

        stdout, stderr = process.communicate(input=pdf_data)
        end_time = time.time()

        if process.returncode == 0:
            # Write the markdown output to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(stdout.decode('utf-8'))

            file_size = os.path.getsize(output_file)
            return True, end_time - start_time, file_size, ""
        else:
            error_msg = stderr.decode('utf-8') if stderr else "Unknown error"
            return False, end_time - start_time, 0, error_msg

    except (OSError, subprocess.SubprocessError, UnicodeDecodeError) as e:
        return False, 0, 0, str(e)

def convert_single_pdf(pdf_filename):
    """Convert a single PDF file to Markdown"""

    # Check if file exists in pdfs directory
    pdf_path = os.path.join("pdfs", pdf_filename)
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        print("Available PDF files:")
        pdf_files = [f for f in os.listdir("pdfs") if f.lower().endswith('.pdf')]
        for f in sorted(pdf_files):
            print(f"   - {f}")
        return False

    # Prepare output
    pdf_name = Path(pdf_filename).stem
    output_dir = "converted"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{pdf_name}.md")

    print(f"🔄 Converting: {pdf_filename}")
    print(f"📄 Input: {pdf_path}")
    print(f"📝 Output: {output_file}")
    print("-" * 40)

    success, duration, file_size, error = convert_pdf_direct(pdf_path, output_file)

    if success:
        print("✅ Conversion successful!")
        print(f"   ⏱️  Time: {duration:.1f} seconds")
        print(f"   📊 Output size: {file_size:,} bytes")
        print(f"   📁 Saved to: {output_file}")
        return True
    else:
        print("❌ Conversion failed!")
        if error:
            print(f"   Error: {error}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_direct.py <pdf_filename>")
        print("\nAvailable PDF files:")
        if os.path.exists("pdfs"):
            pdf_files = [f for f in os.listdir("pdfs") if f.lower().endswith('.pdf')]
            for f in sorted(pdf_files):
                print(f"   - {f}")
        else:
            print("   No pdfs/ directory found!")
        return

    pdf_filename = sys.argv[1]
    convert_single_pdf(pdf_filename)

if __name__ == "__main__":
    main()
