#!/usr/bin/env python3
"""
Cleanup Script for MarkPDFDown Workspace
Removes backup files created by workspace linting

Enterprise Enhancement for MarkPDFDown
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

This file is part of the enterprise enhancement suite for MarkPDFDown,
providing automated cleanup utilities to remove backup files created
during workspace linting operations.

Author: Joseph Wright (github: ch0t4nk)
Created: July 16, 2025
Version: 1.0
"""

import sys
from pathlib import Path

def cleanup_backups():
    """Remove all .backup files from the workspace"""
    root_dir = Path(__file__).parent
    backup_files = list(root_dir.rglob("*.backup"))

    if not backup_files:
        print("✅ No backup files found - workspace is already clean!")
        return

    print(f"🧹 Found {len(backup_files)} backup files to remove:")

    for backup_file in backup_files:
        relative_path = backup_file.relative_to(root_dir)
        print(f"   🗑️  {relative_path}")
        backup_file.unlink()

    print(f"\n✅ Cleaned up {len(backup_files)} backup files!")

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("🧹 MarkPDFDown Backup Cleanup")
        print("\nUsage:")
        print("  python cleanup_backups.py")
        print("\nThis will remove all .backup files created by workspace_lint.py")
        return

    cleanup_backups()

if __name__ == "__main__":
    main()
