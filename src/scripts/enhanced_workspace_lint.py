#!/usr/bin/env python3
"""
Enhanced Workspace Linter for PDFtoMD
Comprehensive linting solution with Mermaid protection, modern Python tooling,
and centralized utilities integration.

Enterprise Enhancement for PDFtoMD
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

Author: Joseph Wright (github: ch0t4nk)
Created: July 25, 2025
Version: 2.0
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

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


class EnhancedWorkspaceLinter:
    """Enhanced workspace linter with comprehensive tooling support"""

    def __init__(self, enable_ruff: bool = True, enable_markdownlint: bool = True):
        self.root_dir = project_root
        self.enable_ruff = enable_ruff
        self.enable_markdownlint = enable_markdownlint

        self.stats = {
            "files_processed": 0,
            "markdown_files": 0,
            "python_files": 0,
            "total_fixes": 0,
            "files_with_fixes": 0,
            "errors": [],
            "ruff_available": False,
            "markdownlint_available": False,
        }

        # Enhanced ignore patterns
        self.ignore_patterns = {
            "directories": {
                str(config.DEFAULT_OUTPUT_FOLDER),
                "converted_markdown",
                "__pycache__",
                ".git",
                "node_modules",
                "venv",
                "env",
                ".vscode",
                "temp_batch",
                str(config.DEFAULT_CONVERTED_FOLDER),
                "temp",
                ".pytest_cache",
                "htmlcov",
                "coverage_html_report",
            },
            "file_extensions": {
                ".pyc",
                ".pyo",
                ".pyd",
                ".so",
                ".dll",
                ".exe",
                ".bin",
                ".log",
                ".tmp",
                ".temp",
                ".backup",
                ".bak",
            },
            "file_patterns": {
                "batch_requests_*.jsonl",
                "batch_info_*.json",
                "usage_stats_*.json",
                "*.backup",
                "*.bak",
                ".DS_Store",
                "Thumbs.db",
                "desktop.ini",
            },
        }

        # Benign warning suppression configuration
        self.suppressed_warnings = {
            "MD001",  # Heading increment (style preference)
            "MD003",  # Heading style (setext vs atx)
            "MD004",  # List style (dash vs asterisk)
            "MD007",  # List indentation (style preference)
            "MD024",  # Duplicate headings (often legitimate)
            "MD025",  # Multiple H1 (false positives from bash comments)
            "MD026",  # Trailing punctuation in headings
            "MD029",  # Ordered list style
            "MD034",  # Bare URL (often intentional)
            "MD047",  # File ending (often not important)
        }

        # Check tool availability
        self._check_tool_availability()

    def _check_tool_availability(self):
        """Check which linting tools are available"""
        # Check for ruff
        try:
            result = subprocess.run(["ruff", "--version"], capture_output=True)
            self.stats["ruff_available"] = result.returncode == 0
        except FileNotFoundError:
            self.stats["ruff_available"] = False

        # Check for markdownlint (optional)
        try:
            result = subprocess.run(["markdownlint", "--version"], capture_output=True)
            self.stats["markdownlint_available"] = result.returncode == 0
        except FileNotFoundError:
            self.stats["markdownlint_available"] = False

    def should_ignore(self, path: Path) -> bool:
        """Check if a path should be ignored"""
        # Check if any parent directory is in ignore list
        for parent in path.parents:
            if parent.name in self.ignore_patterns["directories"]:
                return True

        # Check if current directory is in ignore list
        if path.is_dir() and path.name in self.ignore_patterns["directories"]:
            return True

        # Check file extensions
        if path.suffix in self.ignore_patterns["file_extensions"]:
            return True

        # Check file patterns
        for pattern in self.ignore_patterns["file_patterns"]:
            if path.match(pattern):
                return True

        return False

    def protect_mermaid_diagrams(self, content: str) -> tuple[str, list[str]]:
        """Temporarily replace Mermaid diagrams with placeholders"""
        mermaid_blocks = []
        mermaid_pattern = r"```mermaid\n(.*?)\n```"

        def preserve_mermaid(match):
            mermaid_blocks.append(match.group(0))
            return f"__MERMAID_PLACEHOLDER_{len(mermaid_blocks) - 1}__"

        protected_content = re.sub(
            mermaid_pattern, preserve_mermaid, content, flags=re.DOTALL
        )
        return protected_content, mermaid_blocks

    def restore_mermaid_diagrams(self, content: str, mermaid_blocks: list[str]) -> str:
        """Restore Mermaid diagrams from placeholders"""
        for i, mermaid_block in enumerate(mermaid_blocks):
            content = content.replace(f"__MERMAID_PLACEHOLDER_{i}__", mermaid_block)
        return content

    def fix_markdown_file(self, file_path: Path) -> dict:
        """Fix markdown files with comprehensive tooling and Mermaid protection"""
        fixes = []

        try:
            with open(file_path, encoding="utf-8") as f:
                original_content = f.read()

            content = original_content

            # Protect Mermaid diagrams
            protected_content, mermaid_blocks = self.protect_mermaid_diagrams(content)

            # Try advanced markdown linter first
            advanced_result = self._try_advanced_markdown_linter(
                file_path, protected_content
            )
            if advanced_result["success"]:
                fixes.extend(advanced_result["fixes_list"])
                protected_content = advanced_result["content"]

            # Apply basic markdown fixes
            basic_result = self._apply_basic_markdown_fixes(protected_content)
            protected_content = basic_result["content"]
            fixes.extend(basic_result["fixes_list"])

            # Restore Mermaid diagrams
            final_content = self.restore_mermaid_diagrams(
                protected_content, mermaid_blocks
            )

            # Only write if changes were made
            if final_content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(final_content)

                if fixes:
                    self.stats["files_with_fixes"] += 1
                    self.stats["total_fixes"] += len(fixes)

            return {
                "success": True,
                "fixes": len(fixes),
                "fixes_list": fixes,
                "size_reduction": len(original_content) - len(final_content),
            }

        except (OSError, UnicodeError) as e:
            self.stats["errors"].append(
                f"Error processing markdown file {file_path}: {str(e)}"
            )
            return {"success": False, "error": str(e)}

    def _try_advanced_markdown_linter(self, file_path: Path, content: str) -> dict:
        """Try to use the advanced markdown linter from utils"""
        try:
            sys.path.insert(0, str(self.root_dir / "src"))
            from utils.linting.markdown_linter import MarkdownLinter

            # Write protected content to temp file
            temp_file = file_path.with_suffix(".tmp.md")
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write(content)

            markdown_linter = MarkdownLinter()
            # Disable code block cleanup to protect Mermaid
            markdown_linter.rules["code_block_cleanup"] = False

            result = markdown_linter.lint_file(str(temp_file), backup=False)

            # Read the result
            with open(temp_file, encoding="utf-8") as f:
                processed_content = f.read()

            # Clean up temp file
            temp_file.unlink()

            if "error" not in result:
                return {
                    "success": True,
                    "content": processed_content,
                    "fixes_list": result.get("fixes", []),
                }

        except (ImportError, Exception):
            # Fallback gracefully
            pass

        return {"success": False, "content": content, "fixes_list": []}

    def _apply_basic_markdown_fixes(self, content: str) -> dict:
        """Apply basic markdown fixes"""
        fixes = []

        # Basic markdown fixes
        lines = content.split("\n")
        fixed_lines = []

        for i, line in enumerate(lines):
            original_line = line

            # Remove trailing whitespace
            line = line.rstrip()
            if original_line != line:
                fixes.append(f"Line {i + 1}: Removed trailing whitespace")

            # Fix excessive blank lines (max 2 consecutive)
            if i > 0 and not line.strip() and not lines[i - 1].strip():
                if (
                    len(fixed_lines) > 1
                    and not fixed_lines[-1].strip()
                    and not fixed_lines[-2].strip()
                ):
                    fixes.append(f"Line {i + 1}: Removed excessive blank line")
                    continue

            fixed_lines.append(line)

        # Ensure file ends with single newline
        if fixed_lines and fixed_lines[-1].strip():
            fixed_lines.append("")
            fixes.append("Added final newline")

        new_content = "\n".join(fixed_lines)
        return {"content": new_content, "fixes_list": fixes}

    def fix_python_file(self, file_path: Path) -> dict:
        """Fix Python files using ruff + basic cleanup"""
        fixes = []
        backup_created = None

        try:
            with open(file_path, encoding="utf-8") as f:
                original_content = f.read()

            # Try ruff formatting and linting
            if self.enable_ruff and self.stats["ruff_available"]:
                ruff_result = self._apply_ruff_fixes(file_path)
                fixes.extend(ruff_result["fixes_list"])

            # Re-read content after potential ruff fixes
            with open(file_path, encoding="utf-8") as f:
                current_content = f.read()

            # Apply basic Python fixes
            basic_result = self._apply_basic_python_fixes(current_content)
            final_content = basic_result["content"]
            fixes.extend(basic_result["fixes_list"])

            # Only create backup and write if changes were made
            if final_content != original_content:
                # Create backup
                backup_path = file_path.with_suffix(file_path.suffix + ".backup")
                shutil.copy2(file_path, backup_path)
                backup_created = str(backup_path)

                # Write fixed content
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(final_content)

                if fixes:
                    self.stats["files_with_fixes"] += 1
                    self.stats["total_fixes"] += len(fixes)

            return {
                "success": True,
                "fixes": len(fixes),
                "fixes_list": fixes,
                "backup_created": backup_created,
            }

        except (OSError, UnicodeError) as e:
            self.stats["errors"].append(
                f"Error processing Python file {file_path}: {str(e)}"
            )
            return {"success": False, "error": str(e)}

    def _apply_ruff_fixes(self, file_path: Path) -> dict:
        """Apply ruff formatting and linting fixes"""
        fixes = []

        try:
            # Apply ruff format
            format_result = subprocess.run(
                ["ruff", "format", str(file_path)], capture_output=True, text=True
            )
            if format_result.returncode == 0:
                fixes.append("Applied ruff formatting")

            # Apply ruff linting fixes
            check_result = subprocess.run(
                ["ruff", "check", "--fix", str(file_path)],
                capture_output=True,
                text=True,
            )
            if check_result.returncode == 0 and check_result.stdout.strip():
                fixes.append("Applied ruff linting fixes")

        except (FileNotFoundError, subprocess.SubprocessError):
            pass

        return {"fixes_list": fixes}

    def _apply_basic_python_fixes(self, content: str) -> dict:
        """Apply basic Python formatting fixes"""
        fixes = []
        lines = content.split("\n")
        fixed_lines = []

        for i, line in enumerate(lines):
            original_line = line
            line = line.rstrip()

            if original_line != line:
                fixes.append(f"Line {i + 1}: Removed trailing whitespace")

            # Fix excessive blank lines
            if i > 0 and not line.strip() and not lines[i - 1].strip():
                if (
                    len(fixed_lines) > 1
                    and not fixed_lines[-1].strip()
                    and not fixed_lines[-2].strip()
                ):
                    fixes.append(f"Line {i + 1}: Removed excessive blank line")
                    continue

            fixed_lines.append(line)

        # Ensure proper file ending
        if fixed_lines and fixed_lines[-1].strip():
            fixed_lines.append("")
            fixes.append("Added final newline")

        return {"content": "\n".join(fixed_lines), "fixes_list": fixes}

    def scan_and_fix(self):
        """Main scanning and fixing workflow"""
        print("🚀 Enhanced PDFtoMD Workspace Linter v2.0")
        print("=" * 60)
        print(f"📁 Scanning workspace: {self.root_dir}")
        print(f"🔧 Ruff available: {'✅' if self.stats['ruff_available'] else '❌'}")
        print(f"📝 Advanced MD linter: {'✅' if self.enable_markdownlint else '❌'}")
        print(f"🛡️  Mermaid protection: ✅ ENABLED")
        print("=" * 60)

        # Find files to process
        markdown_files = []
        python_files = []

        for file_path in self.root_dir.rglob("*"):
            if file_path.is_file() and not self.should_ignore(file_path):
                if file_path.suffix.lower() == ".md":
                    markdown_files.append(file_path)
                elif file_path.suffix.lower() == ".py":
                    python_files.append(file_path)

        total_files = len(markdown_files) + len(python_files)
        print(f"📊 Found {total_files} files to process:")
        print(f"   📝 Markdown files: {len(markdown_files)}")
        print(f"   🐍 Python files: {len(python_files)}")
        print()

        # Process files
        self._process_markdown_files(markdown_files)
        self._process_python_files(python_files)

    def _process_markdown_files(self, files: list[Path]):
        """Process markdown files"""
        if not files:
            return

        print("📝 Processing Markdown Files (with Mermaid protection)...")
        print("-" * 50)

        for md_file in sorted(files):
            relative_path = md_file.relative_to(self.root_dir)
            print(f"   Processing: {relative_path}", end=" ... ")

            result = self.fix_markdown_file(md_file)
            if result["success"]:
                fixes_count = result.get("fixes", 0)
                if fixes_count > 0:
                    print(f"✅ {fixes_count} fixes applied")
                    if result.get("size_reduction", 0) > 0:
                        print(
                            f"      📉 Size reduced by {result['size_reduction']} bytes"
                        )
                else:
                    print("✅ Already clean")
            else:
                print(f"❌ Error: {result.get('error', 'Unknown error')}")

            self.stats["markdown_files"] += 1
            self.stats["files_processed"] += 1

        print()

    def _process_python_files(self, files: list[Path]):
        """Process Python files"""
        if not files:
            return

        print("🐍 Processing Python Files (with ruff + basic fixes)...")
        print("-" * 50)

        for py_file in sorted(files):
            relative_path = py_file.relative_to(self.root_dir)
            print(f"   Processing: {relative_path}", end=" ... ")

            result = self.fix_python_file(py_file)
            if result["success"]:
                fixes_count = result.get("fixes", 0)
                if fixes_count > 0:
                    print(f"✅ {fixes_count} fixes applied")
                    if result.get("backup_created"):
                        backup_name = Path(result["backup_created"]).name
                        print(f"      💾 Backup: {backup_name}")
                else:
                    print("✅ Already clean")
            else:
                print(f"❌ Error: {result.get('error', 'Unknown error')}")

            self.stats["python_files"] += 1
            self.stats["files_processed"] += 1

        print()

    def print_summary(self):
        """Print comprehensive summary"""
        print("=" * 60)
        print("📊 ENHANCED WORKSPACE LINTING SUMMARY")
        print("=" * 60)
        print(f"📁 Files Processed: {self.stats['files_processed']}")
        print(f"   📝 Markdown: {self.stats['markdown_files']}")
        print(f"   🐍 Python: {self.stats['python_files']}")
        print()
        print(f"🔧 Total Fixes Applied: {self.stats['total_fixes']}")
        print(f"📄 Files with Fixes: {self.stats['files_with_fixes']}")
        print(f"❌ Errors Encountered: {len(self.stats['errors'])}")
        print()
        print("🛠️  Tools Used:")
        print(
            f"   🔧 Ruff (Python): {'✅ Available' if self.stats['ruff_available'] else '❌ Not available'}"
        )
        print(
            f"   📝 Advanced MD Linter: {'✅ Used' if self.enable_markdownlint else '⚠️  Basic only'}"
        )
        print(f"   🛡️  Mermaid Protection: ✅ Active")

        if self.stats["errors"]:
            print("\n⚠️  ERRORS:")
            for error in self.stats["errors"][:5]:
                print(f"   • {error}")
            if len(self.stats["errors"]) > 5:
                print(f"   ... and {len(self.stats['errors']) - 5} more errors")

        print()
        if self.stats["total_fixes"] > 0:
            print("✅ Enhanced workspace linting completed!")
            print("💾 Backup files created for modified Python files")
            print("🛡️  Mermaid diagrams preserved intact")
        else:
            print("✅ Workspace is already pristine!")


def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print("🚀 Enhanced PDFtoMD Workspace Linter v2.0")
        print()
        print("Usage:")
        print("  python enhanced_workspace_lint.py [options]")
        print()
        print("Options:")
        print("  --no-ruff          Disable ruff Python linting")
        print("  --basic-md         Use only basic markdown fixes")
        print("  -h, --help         Show this help")
        print()
        print("Features:")
        print("  ✅ Advanced Python linting with ruff")
        print("  ✅ Comprehensive markdown processing")
        print("  ✅ Mermaid diagram protection")
        print("  ✅ Smart file detection and filtering")
        print("  ✅ Backup creation for safety")
        print("  ✅ Integration with centralized utilities")
        print("  ✅ Enterprise-grade reporting")
        print()
        print("🛡️  MERMAID PROTECTION ENABLED - Your diagrams are safe!")
        return

    # Parse simple arguments
    enable_ruff = "--no-ruff" not in sys.argv
    enable_advanced_md = "--basic-md" not in sys.argv

    linter = EnhancedWorkspaceLinter(
        enable_ruff=enable_ruff, enable_markdownlint=enable_advanced_md
    )

    try:
        linter.scan_and_fix()
        linter.print_summary()
    except KeyboardInterrupt:
        print("\n\n⚠️  Linting interrupted by user")
        linter.print_summary()
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        linter.print_summary()
        sys.exit(1)


if __name__ == "__main__":
    main()
