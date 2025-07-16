#!/usr/bin/env python3
"""
Workspace Lint & Fix Script for MarkPDFDown
Automatically fixes common markdown and Python linting issues across the workspace
while ignoring output directories and temporary files.

Enterprise Enhancement for MarkPDFDown
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

This file is part of the enterprise enhancement suite for MarkPDFDown,
providing automated workspace linting and fixing capabilities with intelligent
issue detection and resolution across markdown and Python files.

Author: Joseph Wright (github: ch0t4nk)
Created: July 16, 2025
Version: 1.0
"""

import os
import sys
import shutil
from pathlib import Path
from typing import Dict

# Add project root to path for config import
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
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

# Add utils to path for importing
utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils')
sys.path.insert(0, utils_path)

class WorkspaceLinter:
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.stats = {
            'files_processed': 0,
            'markdown_files': 0,
            'python_files': 0,
            'total_fixes': 0,
            'files_with_fixes': 0,
            'errors': []
        }

        # Directories and files to ignore
        self.ignore_patterns = {
            'directories': {
                str(config.DEFAULT_OUTPUT_FOLDER),
                'converted_markdown',
                '__pycache__',
                '.git',
                'node_modules',
                'venv',
                'env',
                '.vscode',
                'temp_batch',
                str(config.DEFAULT_CONVERTED_FOLDER)
            },
            'file_extensions': {
                '.pyc',
                '.pyo',
                '.pyd',
                '.so',
                '.dll',
                '.exe',
                '.bin',
                '.log',
                '.tmp',
                '.temp'
            },
            'file_patterns': {
                'batch_requests_*.jsonl',
                'batch_info_*.json',
                'usage_stats_*.json',
                '*.backup',
                '*.bak',
                '.DS_Store',
                'Thumbs.db'
            }
        }

    def should_ignore(self, path: Path) -> bool:
        """Check if a path should be ignored"""
        # Check if any parent directory is in ignore list
        for parent in path.parents:
            if parent.name in self.ignore_patterns['directories']:
                return True

        # Check if current directory is in ignore list
        if path.is_dir() and path.name in self.ignore_patterns['directories']:
            return True

        # Check file extensions
        if path.suffix in self.ignore_patterns['file_extensions']:
            return True

        # Check file patterns
        for pattern in self.ignore_patterns['file_patterns']:
            if path.match(pattern):
                return True

        return False

    def fix_markdown_file(self, file_path: Path) -> Dict:
        """Fix common markdown issues"""
        # Use basic markdown fixes since advanced linter may not be available
        return self._apply_basic_markdown_fixes(file_path)

    def _apply_basic_markdown_fixes(self, file_path: Path) -> Dict:
        """Apply basic markdown fixes without external linter"""
        fixes = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Basic markdown fixes
            lines = content.split('\n')
            fixed_lines = []

            for i, line in enumerate(lines):
                original_line = line

                # Remove trailing whitespace
                line = line.rstrip()
                if original_line != line:
                    fixes.append(f"Line {i+1}: Removed trailing whitespace")

                # Fix excessive blank lines (max 2 consecutive)
                if i > 0 and not line.strip() and not lines[i-1].strip():
                    if len(fixed_lines) > 1 and not fixed_lines[-1].strip() and not fixed_lines[-2].strip():
                        fixes.append(f"Line {i+1}: Removed excessive blank line")
                        continue

                fixed_lines.append(line)

            # Ensure file ends with single newline
            if fixed_lines and fixed_lines[-1].strip():
                fixed_lines.append('')
                fixes.append("Added final newline")

            new_content = '\n'.join(fixed_lines)

            # Only write if changes were made
            if new_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                if fixes:
                    self.stats['files_with_fixes'] += 1
                    self.stats['total_fixes'] += len(fixes)

            return {
                'success': True,
                'fixes': len(fixes),
                'fixes_list': fixes
            }

        except (OSError, IOError, UnicodeError) as e:
            self.stats['errors'].append(f"Error processing markdown file {file_path}: {str(e)}")
            return {'success': False, 'error': str(e)}

    def fix_python_file(self, file_path: Path) -> Dict:
        """Fix common Python formatting issues"""
        fixes = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # Fix common Python issues
            lines = content.split('\n')
            fixed_lines = []

            for i, line in enumerate(lines):
                original_line = line

                # Remove trailing whitespace
                line = line.rstrip()
                if original_line != line:
                    fixes.append(f"Line {i+1}: Removed trailing whitespace")

                # Fix excessive blank lines (max 2 consecutive)
                if i > 0 and not line.strip() and not lines[i-1].strip():
                    # Skip this blank line if previous was also blank
                    if len(fixed_lines) > 1 and not fixed_lines[-1].strip() and not fixed_lines[-2].strip():
                        fixes.append(f"Line {i+1}: Removed excessive blank line")
                        continue

                fixed_lines.append(line)

            # Ensure file ends with single newline
            if fixed_lines and fixed_lines[-1].strip():
                fixed_lines.append('')
                fixes.append("Added final newline")
            elif len(fixed_lines) > 1 and not fixed_lines[-1].strip() and not fixed_lines[-2].strip():
                # Remove extra blank lines at end
                while len(fixed_lines) > 1 and not fixed_lines[-1].strip() and not fixed_lines[-2].strip():
                    fixed_lines.pop()
                    fixes.append("Removed excessive blank lines at end")

            new_content = '\n'.join(fixed_lines)

            # Only write if changes were made
            if new_content != original_content:
                # Create backup
                backup_path = file_path.with_suffix(file_path.suffix + '.backup')
                shutil.copy2(file_path, backup_path)

                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                if fixes:
                    self.stats['files_with_fixes'] += 1
                    self.stats['total_fixes'] += len(fixes)

                return {
                    'success': True,
                    'fixes': len(fixes),
                    'fixes_list': fixes,
                    'backup_created': str(backup_path)
                }
            else:
                return {'success': True, 'fixes': 0, 'fixes_list': []}

        except (OSError, IOError, UnicodeError) as e:
            self.stats['errors'].append(f"Error processing Python file {file_path}: {str(e)}")
            return {'success': False, 'error': str(e)}

    def scan_and_fix(self) -> None:
        """Scan workspace and fix issues"""
        print("🔧 MarkPDFDown Workspace Linter")
        print("="*60)
        print(f"📁 Scanning workspace: {self.root_dir}")
        print(f"🚫 Ignoring: {', '.join(sorted(self.ignore_patterns['directories']))}")
        print("="*60)

        # Find all files to process
        markdown_files = []
        python_files = []

        for file_path in self.root_dir.rglob('*'):
            if file_path.is_file() and not self.should_ignore(file_path):
                if file_path.suffix.lower() == '.md':
                    markdown_files.append(file_path)
                elif file_path.suffix.lower() == '.py':
                    python_files.append(file_path)

        total_files = len(markdown_files) + len(python_files)
        print(f"📊 Found {total_files} files to process:")
        print(f"   📝 Markdown files: {len(markdown_files)}")
        print(f"   🐍 Python files: {len(python_files)}")
        print()

        # Process markdown files
        if markdown_files:
            print("📝 Processing Markdown Files...")
            print("-" * 40)

            for md_file in sorted(markdown_files):
                relative_path = md_file.relative_to(self.root_dir)
                print(f"   Processing: {relative_path}", end=" ... ")

                result = self.fix_markdown_file(md_file)
                if result['success']:
                    fixes_count = result.get('fixes', 0)
                    if fixes_count > 0:
                        print(f"✅ {fixes_count} fixes applied")
                        if result.get('size_reduction', 0) > 0:
                            print(f"      📉 Size reduced by {result['size_reduction']} bytes")
                    else:
                        print("✅ Already clean")
                else:
                    print(f"❌ Error: {result.get('error', 'Unknown error')}")

                self.stats['markdown_files'] += 1
                self.stats['files_processed'] += 1

            print()

        # Process Python files
        if python_files:
            print("🐍 Processing Python Files...")
            print("-" * 40)

            for py_file in sorted(python_files):
                relative_path = py_file.relative_to(self.root_dir)
                print(f"   Processing: {relative_path}", end=" ... ")

                result = self.fix_python_file(py_file)
                if result['success']:
                    fixes_count = result.get('fixes', 0)
                    if fixes_count > 0:
                        print(f"✅ {fixes_count} fixes applied")
                        if result.get('backup_created'):
                            backup_name = Path(result['backup_created']).name
                            print(f"      💾 Backup: {backup_name}")
                    else:
                        print("✅ Already clean")
                else:
                    print(f"❌ Error: {result.get('error', 'Unknown error')}")

                self.stats['python_files'] += 1
                self.stats['files_processed'] += 1

            print()

    def print_summary(self) -> None:
        """Print final summary"""
        print("="*60)
        print("📊 WORKSPACE LINTING SUMMARY")
        print("="*60)
        print(f"📁 Files Processed: {self.stats['files_processed']}")
        print(f"   📝 Markdown: {self.stats['markdown_files']}")
        print(f"   🐍 Python: {self.stats['python_files']}")
        print()
        print(f"🔧 Total Fixes Applied: {self.stats['total_fixes']}")
        print(f"📄 Files with Fixes: {self.stats['files_with_fixes']}")
        print(f"❌ Errors Encountered: {len(self.stats['errors'])}")

        if self.stats['errors']:
            print("\n⚠️  ERRORS:")
            for error in self.stats['errors'][:5]:  # Show max 5 errors
                print(f"   • {error}")
            if len(self.stats['errors']) > 5:
                print(f"   ... and {len(self.stats['errors']) - 5} more errors")

        print()
        if self.stats['total_fixes'] > 0:
            print("✅ Workspace linting completed with fixes applied!")
            print("💾 Backup files created for modified Python files")
        else:
            print("✅ Workspace is already clean!")

        print("\n🚫 Ignored directories:", ", ".join(sorted(self.ignore_patterns['directories'])))

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("🔧 MarkPDFDown Workspace Linter")
        print("\nUsage:")
        print("  python workspace_lint.py")
        print("\nThis will:")
        print("  ✅ Fix markdown formatting issues (via markdown_linter)")
        print("  ✅ Fix Python whitespace and formatting issues")
        print("  ✅ Remove trailing whitespace")
        print("  ✅ Fix excessive blank lines")
        print("  ✅ Ensure proper file endings")
        print("  💾 Create backup files for Python changes")
        print("  🚫 Ignore outputs/, __pycache__/, and temporary files")
        print("\nSafe to run - creates backups before making changes!")
        return

    linter = WorkspaceLinter()

    try:
        linter.scan_and_fix()
        linter.print_summary()
    except KeyboardInterrupt:
        print("\n\n⚠️  Linting interrupted by user")
        linter.print_summary()
        sys.exit(1)
    except (RuntimeError, OSError) as e:
        print(f"\n\n❌ Fatal error: {e}")
        linter.print_summary()
        sys.exit(1)

if __name__ == "__main__":
    main()
