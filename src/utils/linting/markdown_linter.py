#!/usr/bin/env python3
"""
Fast Local Markdown Linter for PDF Conversions
Fixes common issues in converted markdown files without using OpenAI API
"""

import argparse
import os
import re
import sys
from pathlib import Path


class MarkdownLinter:
    """Fast local markdown linter for PDF conversion outputs"""

    def __init__(self):
        self.fixes_applied = []
        self.rules = {
            "excessive_newlines": True,
            "table_formatting": True,
            "header_spacing": True,
            "list_formatting": True,
            "code_block_cleanup": True,
            "image_alt_text": True,
            "link_formatting": True,
            "whitespace_cleanup": True,
            "pdf_artifacts": True,
            "section_numbering": True,
        }

    def lint_file(self, file_path: str, backup: bool = True) -> dict:
        """Lint a single markdown file"""
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}

        print(f"🔍 Linting: {os.path.basename(file_path)}")

        # Read original content
        with open(file_path, encoding="utf-8") as f:
            original_content = f.read()

        # Create backup if requested
        backup_path = None
        if backup:
            backup_path = f"{file_path}.backup"
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(original_content)

        # Apply fixes
        content = original_content
        self.fixes_applied = []

        content = self._fix_excessive_newlines(content)
        content = self._fix_header_spacing(content)
        content = self._fix_table_formatting(content)
        content = self._fix_list_formatting(content)
        content = self._fix_code_blocks(content)
        content = self._fix_image_alt_text(content)
        content = self._fix_link_formatting(content)
        content = self._fix_pdf_artifacts(content)
        content = self._fix_whitespace(content)
        content = self._fix_section_numbering(content)

        # Write fixed content
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Calculate changes
        lines_before = len(original_content.splitlines())
        lines_after = len(content.splitlines())
        size_before = len(original_content)
        size_after = len(content)

        return {
            "fixes": self.fixes_applied,
            "lines_before": lines_before,
            "lines_after": lines_after,
            "size_before": size_before,
            "size_after": size_after,
            "backup_created": backup_path if backup else None,
        }

    def _fix_excessive_newlines(self, content: str) -> str:
        """Fix excessive blank lines (3+ newlines → 2 newlines)"""
        original_content = content
        # Replace 3+ consecutive newlines with exactly 2
        content = re.sub(r"\n{3,}", "\n\n", content)

        if content != original_content:
            self.fixes_applied.append("Reduced excessive blank lines")
        return content

    def _fix_header_spacing(self, content: str) -> str:
        """Ensure proper spacing around headers"""
        original_content = content
        lines = content.split("\n")
        fixed_lines = []

        for i, line in enumerate(lines):
            # Check if current line is a header
            if re.match(r"^#{1,6}\s+", line):
                # Ensure blank line before header (unless it's the first line)
                if i > 0 and fixed_lines and fixed_lines[-1].strip():
                    fixed_lines.append("")
                fixed_lines.append(line)
                # Ensure blank line after header (unless it's the last line)
                if i < len(lines) - 1 and lines[i + 1].strip():
                    fixed_lines.append("")
            else:
                fixed_lines.append(line)

        content = "\n".join(fixed_lines)
        if content != original_content:
            self.fixes_applied.append("Fixed header spacing")
        return content

    def _fix_table_formatting(self, content: str) -> str:
        """Clean up table formatting"""
        original_content = content

        # Fix table alignment markers
        content = re.sub(
            r"\|\s*[-:]+\s*\|",
            lambda m: "|" + m.group(0)[1:-1].replace(" ", "") + "|",
            content,
        )

        # Ensure tables have proper spacing
        lines = content.split("\n")
        fixed_lines = []
        in_table = False

        for line in lines:
            # Simple check for table rows - contains | and looks like table content
            if (
                "|" in line
                and line.strip().startswith("|")
                and line.strip().endswith("|")
            ):
                if not in_table and fixed_lines and fixed_lines[-1].strip():
                    fixed_lines.append("")
                in_table = True
                fixed_lines.append(line)
            else:
                if in_table and line.strip():
                    fixed_lines.append("")
                in_table = False
                fixed_lines.append(line)

        content = "\n".join(fixed_lines)
        if content != original_content:
            self.fixes_applied.append("Improved table formatting")
        return content

    def _fix_list_formatting(self, content: str) -> str:
        """Fix list item formatting"""
        original_content = content

        # Fix bullet points - ensure space after dash/asterisk
        content = re.sub(r"^(\s*)[-*+]([^\s])", r"\1- \2", content, flags=re.MULTILINE)

        # Fix numbered lists - ensure space after number
        content = re.sub(
            r"^(\s*)(\d+\.)([^\s])", r"\1\2 \3", content, flags=re.MULTILINE
        )

        if content != original_content:
            self.fixes_applied.append("Fixed list formatting")
        return content

    def _fix_code_blocks(self, content: str) -> str:
        """Clean up code block formatting"""
        original_content = content

        # Fix code fences - ensure proper newlines
        content = re.sub(r"```(\w*)\n+", r"```\1\n", content)
        content = re.sub(r"\n+```", r"\n```", content)

        # Fix inline code with excessive backticks
        content = re.sub(r"`{3,}([^`]+)`{3,}", r"`\1`", content)

        if content != original_content:
            self.fixes_applied.append("Cleaned up code blocks")
        return content

    def _fix_image_alt_text(self, content: str) -> str:
        """Improve image alt text"""
        original_content = content

        # Fix empty alt text
        content = re.sub(r"!\[\]\(([^)]+)\)", r"![Image](\1)", content)

        # Fix generic alt text
        content = re.sub(r"!\[image\]\(([^)]+)\)", r"![Image](\1)", content)

        if content != original_content:
            self.fixes_applied.append("Improved image alt text")
        return content

    def _fix_link_formatting(self, content: str) -> str:
        """Clean up link formatting"""
        original_content = content

        # Fix malformed links
        content = re.sub(r"\[([^\]]+)\]\s*\(([^)]+)\)", r"[\1](\2)", content)

        if content != original_content:
            self.fixes_applied.append("Fixed link formatting")
        return content

    def _fix_pdf_artifacts(self, content: str) -> str:
        """Remove common PDF conversion artifacts"""
        original_content = content

        # Remove page numbers at end of lines
        content = re.sub(r"\s+\d+\s*$", "", content, flags=re.MULTILINE)

        # Remove header/footer repeated text
        content = re.sub(r"^(.*?)\n\1$", r"\1", content, flags=re.MULTILINE)

        # Remove excessive punctuation from PDF parsing
        content = re.sub(r"\.{3,}", "...", content)
        content = re.sub(r"-{3,}", "---", content)

        # Remove weird spacing artifacts
        content = re.sub(r"\s+([.,:;!?])", r"\1", content)

        if content != original_content:
            self.fixes_applied.append("Removed PDF artifacts")
        return content

    def _fix_whitespace(self, content: str) -> str:
        """Clean up whitespace issues"""
        original_content = content

        # Remove trailing whitespace
        content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)

        # Fix mixed tabs/spaces
        content = content.replace("\t", "    ")

        # Remove excessive spaces
        content = re.sub(r"  +", " ", content)

        if content != original_content:
            self.fixes_applied.append("Cleaned up whitespace")
        return content

    def _fix_section_numbering(self, content: str) -> str:
        """Fix section numbering in headers"""
        original_content = content

        # Clean up malformed section numbers
        content = re.sub(
            r"^(#{1,6})\s*(\d+\.)+\s*(\d+\.)*\s*", r"\1 ", content, flags=re.MULTILINE
        )

        if content != original_content:
            self.fixes_applied.append("Cleaned section numbering")
        return content

    def lint_directory(
        self, directory: str, pattern: str = "*.md", backup: bool = True
    ) -> dict:
        """Lint all markdown files in a directory"""
        dir_path = Path(directory)
        if not dir_path.exists():
            return {"error": f"Directory not found: {directory}"}

        md_files = list(dir_path.glob(pattern))
        if not md_files:
            return {"error": f"No markdown files found in {directory}"}

        print(f"🔍 Found {len(md_files)} markdown files to lint")

        results = {}
        total_fixes = 0
        total_size_reduction = 0

        for file_path in md_files:
            result = self.lint_file(str(file_path), backup)
            if "error" not in result:
                results[file_path.name] = result
                total_fixes += len(result["fixes"])
                total_size_reduction += result["size_before"] - result["size_after"]

                # Print summary for each file
                if result["fixes"]:
                    print(
                        f"   ✅ {file_path.name}: {len(result['fixes'])} fixes applied"
                    )
                    for fix in result["fixes"]:
                        print(f"      • {fix}")
                else:
                    print(f"   ℹ️ {file_path.name}: No fixes needed")

        return {
            "files_processed": len(results),
            "total_fixes": total_fixes,
            "total_size_reduction": total_size_reduction,
            "results": results,
        }


def main():
    """Command line interface for the markdown linter"""
    parser = argparse.ArgumentParser(
        description="Fast Local Markdown Linter for PDF Conversions"
    )
    parser.add_argument("path", help="File or directory to lint")
    parser.add_argument(
        "--no-backup", action="store_true", help="Skip creating backup files"
    )
    parser.add_argument(
        "--pattern",
        default="*.md",
        help="File pattern for directory linting (default: *.md)",
    )

    args = parser.parse_args()

    linter = MarkdownLinter()

    if os.path.isfile(args.path):
        # Lint single file
        result = linter.lint_file(args.path, backup=not args.no_backup)
        if "error" in result:
            print(f"❌ Error: {result['error']}")
            return 1

        print("\n📊 Linting Results:")
        print(f"   ✅ Fixes applied: {len(result['fixes'])}")
        for fix in result["fixes"]:
            print(f"      • {fix}")
        print(f"   📄 Lines: {result['lines_before']} → {result['lines_after']}")
        print(f"   💾 Size: {result['size_before']:,} → {result['size_after']:,} bytes")
        if result["backup_created"]:
            print(f"   💾 Backup: {result['backup_created']}")

    elif os.path.isdir(args.path):
        # Lint directory
        result = linter.lint_directory(
            args.path, args.pattern, backup=not args.no_backup
        )
        if "error" in result:
            print(f"❌ Error: {result['error']}")
            return 1

        print("\n📊 Directory Linting Results:")
        print(f"   📁 Files processed: {result['files_processed']}")
        print(f"   ✅ Total fixes: {result['total_fixes']}")
        print(f"   💾 Size reduction: {result['total_size_reduction']:,} bytes")
        if not args.no_backup:
            print("   💾 Backups created for all modified files")

    else:
        print(f"❌ Error: Path not found: {args.path}")
        return 1

    print("✅ Linting complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
