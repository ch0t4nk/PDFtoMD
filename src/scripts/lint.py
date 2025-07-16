#!/usr/bin/env python3
"""
MarkPDFDown Workspace Linter Launcher
Convenient access to workspace linting from root directory
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Main entry point for the lint launcher script."""
    # Get the script path - we're in src/scripts/, so workspace_lint.py is in the same directory
    script_path = Path(__file__).parent / "workspace_lint.py"

    if not script_path.exists():
        print("❌ Error: workspace_lint.py not found at expected location")
        print(f"   Expected: {script_path}")
        sys.exit(1)

    # Run the actual linter with all arguments
    try:
        # Set working directory to project root (two levels up from src/scripts/)
        project_root = Path(__file__).parent.parent.parent
        result = subprocess.run([sys.executable, str(script_path)] + sys.argv[1:],
                               cwd=project_root, check=False)
        sys.exit(result.returncode)
    except (subprocess.SubprocessError, OSError) as e:
        print(f"❌ Error running workspace linter: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
