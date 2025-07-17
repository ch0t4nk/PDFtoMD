#!/usr/bin/env python3
"""
Spell Check Validation Script
Validates that all common technical terms in the project are covered by our spell check configuration.
"""

import json
from pathlib import Path


def check_cspell_coverage():
    """Check if our cspell configuration covers common technical terms."""

    # Load cspell configuration
    cspell_path = Path("cspell.json")
    if not cspell_path.exists():
        print("❌ cspell.json not found!")
        return False

    with open(cspell_path, encoding="utf-8") as f:
        cspell_config = json.load(f)

    # Get words from configuration
    configured_words = set(word.lower() for word in cspell_config.get("words", []))

    # Common technical terms that should be covered
    essential_terms = {
        "markpdfdown",
        "multimodal",
        "ssot",
        "llm",
        "openai",
        "pylint",
        "pyproject",
        "toml",
        "asyncio",
        "pathlib",
        "metadata",
        "config",
        "configs",
        "preprocessing",
        "postprocessing",
        "tokenization",
        "embeddings",
        "dockerfile",
        "kubernetes",
        "oauth",
        "https",
        "json",
        "yaml",
        "csv",
        "xml",
        "markdown",
        "cli",
        "api",
        "sdk",
        "restful",
        "webhook",
        "endpoint",
        "pytest",
        "uvicorn",
        "gunicorn",
        "pydantic",
        "tiktoken",
        "aiofiles",
        "conda",
        "pip",
        "vscode",
        "github",
        "gitignore",
        "changelog",
        "readme",
    }

    # Check coverage
    missing_terms = essential_terms - configured_words
    covered_terms = essential_terms & configured_words

    # Report results
    print("🔍 Spell Check Coverage Report")
    print("=" * 50)
    print(f"✅ Covered terms: {len(covered_terms)}/{len(essential_terms)}")
    print(
        f"📊 Coverage percentage: {len(covered_terms) / len(essential_terms) * 100:.1f}%"
    )

    if missing_terms:
        print(f"❌ Missing terms: {sorted(missing_terms)}")
        return False
    else:
        print("🎉 All essential terms are covered!")
        return True


def check_files_exist():
    """Check if all spell check configuration files exist."""
    required_files = [
        "cspell.json",
        ".cspell-dictionaries.txt",
        ".vscode/settings.json",
        "docs/GLOSSARY.md",
    ]

    print("\n📁 Configuration Files Check")
    print("=" * 50)

    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            all_exist = False

    return all_exist


def main():
    """Main validation function."""
    print("🧙‍♂️ MarkPDFDown Spell Check Validation")
    print("=" * 50)

    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ Not in MarkPDFDown project directory!")
        return 1

    # Run checks
    files_ok = check_files_exist()
    coverage_ok = check_cspell_coverage()

    # Final result
    print("\n🎯 Final Result")
    print("=" * 50)

    if files_ok and coverage_ok:
        print("✅ Spell check system is properly configured!")
        print("🚀 Problem count should now be zero for unknown words.")
        return 0
    else:
        print("❌ Issues found with spell check configuration.")
        return 1


if __name__ == "__main__":
    exit(main())
