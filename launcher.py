#!/usr/bin/env python3
"""
Convenience launcher for markpdfdown tools after file reorganization.
Usage: python launcher.py [tool] [args...]

Available tools:
  auto-batch    - Main batch processing script
  workspace-lint - Lint and fix workspace files
  quick-lint    - Quick linting utility
  cleanup       - Cleanup backup files
  cleanup-temp  - Cleanup temporary files and directories
  convert-any   - Convert any file type
  convert-fast  - Fast conversion utility
  optimize-lm   - Optimize LM Studio settings
  test-llm      - Test LLM connection
"""

import sys
import subprocess
from pathlib import Path

# Get the directory containing this script
ROOT_DIR = Path(__file__).parent

# Tool mappings
TOOLS = {
    'auto-batch': 'src/scripts/auto_batch.py',
    'workspace-lint': 'src/scripts/workspace_lint.py', 
    'quick-lint': 'src/scripts/quick_lint.py',
    'cleanup': 'src/scripts/cleanup_backups.py',
    'cleanup-temp': 'cleanup.py',
    'convert-any': 'tools/conversion/convert_any.py',
    'convert-fast': 'tools/conversion/convert_fast.py',
    'optimize-lm': 'tools/optimization/optimize_lm_studio.py',
    'test-llm': 'tools/testing/simple_llm_test.py',
}

def show_help():
    """Show available tools."""
    print(__doc__)
    print("\nExample usage:")
    print("  python launcher.py auto-batch --help")
    print("  python launcher.py workspace-lint")
    print("  python launcher.py convert-any input.pdf")

def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)
    
    tool_name = sys.argv[1]
    
    if tool_name in ['-h', '--help', 'help']:
        show_help()
        sys.exit(0)
        
    if tool_name not in TOOLS:
        print(f"Error: Unknown tool '{tool_name}'")
        print("Run 'python launcher.py help' to see available tools")
        sys.exit(1)
    
    # Get the tool script path
    tool_script = ROOT_DIR / TOOLS[tool_name]
    
    if not tool_script.exists():
        print(f"Error: Tool script not found: {tool_script}")
        sys.exit(1)
    
    # Execute the tool with remaining arguments
    cmd = [sys.executable, str(tool_script)] + sys.argv[2:]
    
    try:
        result = subprocess.run(cmd, cwd=ROOT_DIR, check=False)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
    except (OSError, subprocess.SubprocessError) as e:
        print(f"Error running tool: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
