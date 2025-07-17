#!/usr/bin/env python3
"""
Cleanup Utility - Remove stale temp directories and files.
"""

import importlib.util
import shutil
from pathlib import Path

# Import config
current_dir = Path(__file__).parent
config_path = current_dir / "config.py"

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


def cleanup_temp_directories():
    """Clean up all temporary directories and files"""
    print("🧹 MarkPDFDown Cleanup Utility")
    print("=" * 50)

    temp_folder = Path(str(config.DEFAULT_TEMP_FOLDER))
    cleaned = 0

    if temp_folder.exists():
        print(f"📁 Cleaning temp folder: {temp_folder}")

        # Remove all subdirectories in temp
        for item in temp_folder.iterdir():
            if item.is_dir():
                try:
                    shutil.rmtree(item)
                    print(f"   🗑️  Removed directory: {item.name}")
                    cleaned += 1
                except (OSError, PermissionError) as e:
                    print(f"   ❌ Could not remove {item.name}: {e}")
            elif item.is_file():
                try:
                    item.unlink()
                    print(f"   🗑️  Removed file: {item.name}")
                    cleaned += 1
                except (OSError, PermissionError) as e:
                    print(f"   ❌ Could not remove {item.name}: {e}")

    # Clean up other temp patterns in root
    root_cleanup_patterns = [
        "page_*.jpg",
        "*.jpg",
        "batch_info_*.json",
        "usage_stats_*.json",
        "temp_batch",
    ]

    print("\n📁 Cleaning root directory patterns...")
    for pattern in root_cleanup_patterns:
        for item in Path(".").glob(pattern):
            try:
                if item.is_dir():
                    shutil.rmtree(item)
                    print(f"   🗑️  Removed directory: {item.name}")
                else:
                    item.unlink()
                    print(f"   🗑️  Removed file: {item.name}")
                cleaned += 1
            except (OSError, PermissionError) as e:
                print(f"   ❌ Could not remove {item.name}: {e}")

    print(f"\n✅ Cleanup complete! Removed {cleaned} items.")


if __name__ == "__main__":
    cleanup_temp_directories()
