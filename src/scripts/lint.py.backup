#!/usr/bin/env python3
"""
MarkPDFDown Workspace Linter Launcher
Convenient access to workspace linting from root directory
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get the script path
    script_path = Path(__file__).parent / "src" / "scripts" / "workspace_lint.py"
    
    if not script_path.exists():
        print("❌ Error: workspace_lint.py not found at expected location")
        print(f"   Expected: {script_path}")
        sys.exit(1)
    
    # Run the actual linter with all arguments
    try:
        result = subprocess.run([sys.executable, str(script_path)] + sys.argv[1:], 
                               cwd=Path(__file__).parent)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"❌ Error running workspace linter: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
