#!/usr/bin/env python3
"""
Quick Test Runner for PDFtoMD
=================================

A simple script to run basic validation tests before comprehensive testing.
"""

import subprocess
import sys
from pathlib import Path


def run_quick_validation():
    """Run quick validation checks"""
    print("[TEST] PDFtoMD Quick Validation")
    print("=" * 40)

    errors = []

    # Check Python version
    if sys.version_info < (3, 9):
        errors.append(
            f"Python 3.9+ required, found {sys.version_info.major}.{sys.version_info.minor}"
        )
    else:
        print(
            f"[PASS] Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        )

    # Check required files
    root_dir = Path(__file__).parent
    required_files = [
        "config.py",
        "requirements.txt",
        "test_comprehensive.py",
        ".env.template",
    ]

    for file_path in required_files:
        if (root_dir / file_path).exists():
            print(f"[PASS] {file_path}")
        else:
            errors.append(f"Missing file: {file_path}")
            print(f"[FAIL] {file_path}")

    # Check if comprehensive test script runs
    try:
        result = subprocess.run(
            [sys.executable, "test_comprehensive.py", "structure"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

        if result.returncode == 0:
            print("[PASS] Comprehensive test script executable")
        else:
            errors.append("Comprehensive test script failed")
            print("[FAIL] Comprehensive test script failed")
            print(f"   Error: {result.stderr}")

    except subprocess.TimeoutExpired:
        errors.append("Comprehensive test script timed out")
        print("[FAIL] Comprehensive test script timed out")
    except Exception as e:  # pylint: disable=broad-except
        errors.append(f"Could not run comprehensive test script: {str(e)}")
        print(f"[FAIL] Could not run comprehensive test script: {str(e)}")

    print("=" * 40)

    if errors:
        print("[FAIL] VALIDATION FAILED")
        for error in errors:
            print(f"   • {error}")
        return False
    else:
        print("[PASS] VALIDATION PASSED")
        print("\nRun full test suite with:")
        print("   python test_comprehensive.py")
        return True


if __name__ == "__main__":
    success = run_quick_validation()
    sys.exit(0 if success else 1)
