#!/usr/bin/env python3
"""
Centralized Cleanup Manager for PDFtoMD
Consolidates all cleanup functionality from across the codebase

Enterprise Enhancement for PDFtoMD
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

This module centralizes cleanup functionality that was previously
duplicated across multiple files including batch_api.py, auto_batch.py,
master.py, and cleanup.py.

Author: Joseph Wright (github: ch0t4nk)
Created: July 25, 2025
Version: 1.0
"""

import shutil
import time
from pathlib import Path
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


class CleanupManager:
    """Centralized cleanup utilities for PDFtoMD workspace management"""
    
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.cleaned_count = 0
    
    def log(self, message, force=False):
        """Log message if verbose mode enabled"""
        if self.verbose or force:
            print(message)
    
    def safe_remove_file(self, file_path):
        """Safely remove a file with error handling"""
        try:
            file_path.unlink()
            self.cleaned_count += 1
            self.log(f"   🗑️  Removed: {file_path.name}")
            return True
        except OSError as e:
            self.log(f"   ⚠️  Could not remove {file_path.name}: {e}")
            return False
    
    def safe_remove_directory(self, dir_path):
        """Safely remove a directory and its contents"""
        try:
            if dir_path.is_dir():
                shutil.rmtree(dir_path)
                self.cleaned_count += 1
                self.log(f"   🗑️  Removed directory: {dir_path.name}")
                return True
            else:
                return self.safe_remove_file(dir_path)
        except OSError as e:
            self.log(f"   ⚠️  Could not remove directory {dir_path.name}: {e}")
            return False
    
    def cleanup_batch_files(self):
        """Clean up orphaned batch files (from batch_api.py)"""
        self.log("🧹 Cleaning up orphaned batch files...")
        
        # Clean JSONL files in root (shouldn't exist after our fix)
        root_dir = Path.cwd()
        for jsonl_file in root_dir.glob("batch_requests_*.jsonl"):
            self.safe_remove_file(jsonl_file)
        
        # Clean old batch info files in root (legacy)
        for batch_info in root_dir.glob("batch_info_*.json"):
            self.safe_remove_file(batch_info)
        
        # Clean usage stats files in root (legacy)
        for usage_file in root_dir.glob("usage_stats_*.json"):
            self.safe_remove_file(usage_file)
        
        # Clean temp batch directory and all its contents
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        if temp_batch_dir.exists():
            self.log(f"   🧹 Cleaning temp_batch directory...")
            
            # Remove all JSONL files
            for jsonl_file in temp_batch_dir.glob("batch_requests_*.jsonl"):
                self.safe_remove_file(jsonl_file)
            
            # Remove all batch info files
            for batch_info in temp_batch_dir.glob("batch_info_*.json"):
                self.safe_remove_file(batch_info)
            
            # Remove all PDF-specific subdirectories (temp_batch/pdf_name/)
            for pdf_dir in temp_batch_dir.iterdir():
                if pdf_dir.is_dir():
                    self.safe_remove_directory(pdf_dir)
            
            # Remove the temp_batch directory itself if now empty
            try:
                if not any(temp_batch_dir.iterdir()):
                    temp_batch_dir.rmdir()
                    self.log(f"   🗑️  Removed empty temp_batch directory")
                    self.cleaned_count += 1
            except OSError:
                # Directory not empty or other issue
                remaining_files = list(temp_batch_dir.iterdir())
                if remaining_files:
                    self.log(f"   ⚠️  temp_batch directory still contains {len(remaining_files)} items")
                    for item in remaining_files[:3]:  # Show first 3 items
                        self.log(f"      - {item.name}")
                    if len(remaining_files) > 3:
                        self.log(f"      ... and {len(remaining_files) - 3} more items")
        
        # Clean any page images that might be left in root (legacy issue)
        for page_img in root_dir.glob("page_*.jpg"):
            self.safe_remove_file(page_img)
    
    def cleanup_workspace(self):
        """Clean up workspace temporary files (from auto_batch.py)"""
        self.log("🧹 Cleaning up workspace...")
        
        # Clean up temp directory structure
        temp_dir = config.DEFAULT_TEMP_FOLDER
        if temp_dir and Path(temp_dir).exists():
            temp_batch_dir = Path(temp_dir) / "temp_batch"
            if temp_batch_dir.exists():
                if self.safe_remove_directory(temp_batch_dir):
                    self.log("   🗑️  Removed temp batch directory")
        
        # Remove any remaining files in root (legacy cleanup)
        cleanup_patterns = ["batch_info_*.json", "usage_stats_*.json", "page_*.jpg"]
        
        for pattern in cleanup_patterns:
            for item in Path(".").glob(pattern):
                # Safety check: don't delete session folders or files
                if "session_" in item.name:
                    self.log(f"   ⚠️  Skipped session-related file: {item.name}")
                    continue
                
                if item.is_dir():
                    self.safe_remove_directory(item)
                else:
                    self.safe_remove_file(item)
        
        # Clean up converted directory (moved to session) - only if it's in workspace
        converted_dir = Path(str(config.DEFAULT_CONVERTED_FOLDER))
        if (converted_dir.exists() and 
            converted_dir.is_relative_to(Path.cwd()) and 
            any(converted_dir.iterdir())):
            try:
                shutil.rmtree(converted_dir)
                converted_dir.mkdir(exist_ok=True)  # Recreate empty
                self.cleaned_count += 1
                self.log("   🗑️  Cleaned converted directory")
            except (OSError, PermissionError):
                self.log("   ⚠️  Could not clean converted directory")
    
    def cleanup_temp_files(self):
        """Clean up temporary files and directories (from master.py)"""
        self.log("🧹 Cleaning up temporary files...")
        
        cleanup_patterns = ["batch_requests_*.jsonl", "temp_batch", "batch_info_*.json"]
        
        for pattern in cleanup_patterns:
            if "*" in pattern:
                # Glob pattern
                for item in Path(".").glob(pattern):
                    self.safe_remove_directory(item)
            else:
                # Direct path
                item = Path(pattern)
                if item.exists():
                    self.safe_remove_directory(item)
    
    def cleanup_temp_directories(self):
        """Clean up all temporary directories and files (from cleanup.py)"""
        self.log("🧹 MarkPDFDown Cleanup Utility")
        self.log("=" * 50)
        
        temp_folder = Path(str(config.DEFAULT_TEMP_FOLDER))
        
        if temp_folder.exists():
            self.log(f"📁 Cleaning temp folder: {temp_folder}")
            
            # Remove all subdirectories in temp
            for item in temp_folder.iterdir():
                if item.is_dir():
                    self.safe_remove_directory(item)
                elif item.is_file():
                    self.safe_remove_file(item)
        
        # Clean up other temp patterns in root
        root_cleanup_patterns = [
            "page_*.jpg",
            "*.jpg",
            "batch_info_*.json",
            "usage_stats_*.json",
            "temp_batch",
        ]
        
        self.log("\n📁 Cleaning root directory patterns...")
        for pattern in root_cleanup_patterns:
            for item in Path(".").glob(pattern):
                self.safe_remove_directory(item)
    
    def cleanup_backups(self):
        """Remove all .backup files from the workspace (from cleanup_backups.py)"""
        root_dir = Path(__file__).parent.parent.parent  # Go to project root
        backup_files = list(root_dir.rglob("*.backup"))
        
        if not backup_files:
            self.log("✅ No backup files found - workspace is already clean!")
            return
        
        self.log(f"🧹 Found {len(backup_files)} backup files to remove:")
        
        for backup_file in backup_files:
            relative_path = backup_file.relative_to(root_dir)
            self.log(f"   🗑️  {relative_path}")
            self.safe_remove_file(backup_file)
        
        self.log(f"\n✅ Cleaned up {len(backup_files)} backup files!")
    
    def comprehensive_cleanup(self):
        """Run all cleanup operations"""
        self.log("🧹 Running comprehensive workspace cleanup...")
        self.cleaned_count = 0
        
        self.cleanup_batch_files()
        self.cleanup_workspace()
        self.cleanup_temp_files()
        self.cleanup_temp_directories()
        
        if self.cleaned_count > 0:
            self.log(f"✅ Cleanup completed! Removed {self.cleaned_count} orphaned files.")
        else:
            self.log("✅ No orphaned files found - system is clean!")
        
        return self.cleaned_count


def main():
    """Main entry point for standalone usage"""
    import sys
    
    cleanup_manager = CleanupManager(verbose=True)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "batch":
            cleanup_manager.cleanup_batch_files()
        elif command == "workspace":
            cleanup_manager.cleanup_workspace()
        elif command == "temp":
            cleanup_manager.cleanup_temp_files()
        elif command == "directories":
            cleanup_manager.cleanup_temp_directories()
        elif command == "backups":
            cleanup_manager.cleanup_backups()
        elif command == "all":
            cleanup_manager.comprehensive_cleanup()
        else:
            print("Usage: python cleanup_manager.py [batch|workspace|temp|directories|backups|all]")
            return
    else:
        cleanup_manager.comprehensive_cleanup()


if __name__ == "__main__":
    main()
