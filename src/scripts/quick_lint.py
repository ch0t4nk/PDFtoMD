#!/usr/bin/env python3
"""
Quick Lint Command for PDFtoMD
Fast access to local markdown linting
"""

import os
import sys
from pathlib import Path

# Add parent directories to path
script_dir = Path(__file__).parent
root_dir = script_dir.parent.parent
sys.path.insert(0, str(root_dir))

# Try to import the linter
try:
    from src.utils.linting.markdown_linter import MarkdownLinter
except ImportError:
    print("⚠️  Markdown linter not available")
    sys.exit(1)


def main():
    """Quick lint command"""
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help"]):
        print("🔧 Quick Markdown Linter")
        print("\nUsage:")
        print("  python quick_lint.py <file_or_directory>")
        print("  python quick_lint.py outputs/converted    # Lint all converted files")
        print("  python quick_lint.py file.md              # Lint single file")
        print("\nThis will:")
        print("  ✅ Fix excessive newlines and spacing")
        print("  ✅ Clean up table formatting")
        print("  ✅ Fix header spacing")
        print("  ✅ Improve list formatting")
        print("  ✅ Remove PDF artifacts")
        print("  ✅ Clean up whitespace issues")
        print("  💾 Create .backup files automatically")
        return

    target = sys.argv[1]
    linter = MarkdownLinter()

    print(f"🚀 Quick linting: {target}")

    if os.path.isfile(target):
        # Lint single file
        result = linter.lint_file(target)
        if "error" in result:
            print(f"❌ {result['error']}")
            return

        if result["fixes"]:
            print(f"✅ Applied {len(result['fixes'])} fixes:")
            for fix in result["fixes"]:
                print(f"   • {fix}")
        else:
            print("ℹ️ No fixes needed - file looks good!")

    elif os.path.isdir(target):
        # Lint directory
        result = linter.lint_directory(target)
        if "error" in result:
            print(f"❌ {result['error']}")
            return

        print(f"✅ Processed {result['files_processed']} files")
        print(f"✅ Applied {result['total_fixes']} total fixes")
        if result["total_size_reduction"] > 0:
            print(f"📉 Reduced size by {result['total_size_reduction']:,} bytes")

    else:
        print(f"❌ Path not found: {target}")


if __name__ == "__main__":
    main()
