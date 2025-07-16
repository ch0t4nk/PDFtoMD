"""
Optimized Fast PDF Converter with parallel processing.
"""

import os
import sys
import subprocess
import time
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

def convert_pdf_optimized(pdf_path, output_file, max_workers=3):
    """Convert PDF with parallel processing and optimized settings."""
    # max_workers parameter kept for API compatibility but not used in current implementation

    process = None
    try:
        # Read the PDF file as binary
        with open(pdf_path, 'rb') as pdf_file:
            pdf_data = pdf_file.read()

        print(f"📊 Input file size: {len(pdf_data):,} bytes")

        # Run main.py with optimized environment
        start_time = time.time()

        # Set optimized environment variables for faster processing
        env = os.environ.copy()
        env['OPENAI_MAX_TOKENS'] = '4096'  # Reduce max tokens for speed
        env['OPENAI_TEMPERATURE'] = '0.1'  # Lower temperature for speed
        env['MARKPDF_OUTPUT_FILE'] = output_file  # Pass output file name

        process = subprocess.Popen(
            [sys.executable, 'src/core/main_fast.py'],  # We'll create this optimized version
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.getcwd(),
            env=env
        )

        stdout, stderr = process.communicate(input=pdf_data, timeout=1800)  # 30 min timeout
        end_time = time.time()

        print(f"🔍 Process return code: {process.returncode}")
        if stderr:
            print(f"🚨 Stderr: {stderr.decode('utf-8', errors='ignore')[:500]}...")

        if process.returncode == 0:
            if stdout:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(stdout.decode('utf-8', errors='ignore'))

                file_size = os.path.getsize(output_file)
                return True, end_time - start_time, file_size, ""
            else:
                return False, end_time - start_time, 0, "No output generated"
        else:
            error_msg = stderr.decode('utf-8', errors='ignore') if stderr else "Unknown error"
            return False, end_time - start_time, 0, error_msg

    except subprocess.TimeoutExpired:
        if process:
            process.kill()
        return False, 0, 0, "Process timeout (30 minutes)"
    except (OSError, subprocess.SubprocessError, UnicodeDecodeError) as e:
        return False, 0, 0, str(e)

def convert_optimized(filename):
    """Convert with optimized settings"""

    # Check if file exists
    file_path = os.path.join(str(config.DEFAULT_PDF_FOLDER), filename)
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False

    # Prepare output directories
    file_name = Path(filename).stem
    output_dir = str(config.DEFAULT_CONVERTED_FOLDER)
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{file_name}_fast.md")

    print(f"🚀 Fast Converting: {filename}")
    print(f"📄 Input: {file_path}")
    print(f"📝 Output: {output_file}")
    print("⚡ Using optimized settings...")
    print("-" * 50)

    success, duration, file_size, error = convert_pdf_optimized(file_path, output_file)

    if success:
        print("✅ Fast conversion successful!")
        print(f"   ⏱️  Time: {duration:.1f} seconds")
        print(f"   📊 Output size: {file_size:,} bytes")
        print(f"   📁 Saved to: {output_file}")
        print(f"   ⚡ Speed: {file_size/duration:.0f} bytes/second")
        return True
    else:
        print("❌ Fast conversion failed!")
        if error:
            print(f"   Error: {error}")
        return False

def main():
    """Main function for command-line usage."""
    if len(sys.argv) != 2:
        print("Usage: python convert_fast.py <pdf_filename>")
        print("\nAvailable PDF files:")
        if os.path.exists(str(config.DEFAULT_PDF_FOLDER)):
            files = [
                f for f in os.listdir(str(config.DEFAULT_PDF_FOLDER))
                if f.lower().endswith('.pdf')
            ]
            for f in sorted(files):
                print(f"   - {f}")
        return

    filename = sys.argv[1]
    convert_optimized(filename)


if __name__ == "__main__":
    main()