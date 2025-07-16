#!/usr/bin/env python3
"""
LM Studio Settings Optimizer
Finds and modifies LM Studio configuration files for optimal performance
"""

import json
import shutil
from pathlib import Path
from typing import Dict, Any, List

def find_lm_studio_configs() -> List[Path]:
    """Find all LM Studio configuration files"""
    lm_studio_dir = Path.home() / ".lmstudio"
    config_files = []

    if lm_studio_dir.exists():
        # Look for internal config files
        internal_dir = lm_studio_dir / ".internal"
        if internal_dir.exists():
            config_files.extend(internal_dir.glob("**/*.json"))

        # Look for presets
        preset_dir = lm_studio_dir / "config-presets"
        if preset_dir.exists():
            config_files.extend(preset_dir.glob("*.json"))

    return config_files

def backup_config(config_path: Path) -> None:
    """Create backup of config file"""
    backup_path = config_path.with_suffix(f"{config_path.suffix}.backup")
    if not backup_path.exists():
        shutil.copy2(config_path, backup_path)
        print(f"✅ Backed up: {config_path.name}")

def optimize_config(config_path: Path, optimizations: Dict[str, Any]) -> bool:
    """Apply optimizations to a config file"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # Create backup first
        backup_config(config_path)

        # Apply optimizations
        modified = False
        for key, value in optimizations.items():
            if key in config and config[key] != value:
                print(f"📝 {config_path.name}: {key} {config[key]} → {value}")
                config[key] = value
                modified = True
            elif key not in config:
                print(f"➕ {config_path.name}: Adding {key} = {value}")
                config[key] = value
                modified = True

        if modified:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            return True

        return False

    except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
        print(f"❌ Error processing {config_path}: {e}")
        return False

def create_optimized_preset() -> None:
    """Create an optimized preset file"""
    lm_studio_dir = Path.home() / ".lmstudio"
    preset_dir = lm_studio_dir / "config-presets"

    if not preset_dir.exists():
        preset_dir.mkdir(parents=True, exist_ok=True)

    optimized_preset = {
        "name": "Performance Optimized",
        "description": "Optimized settings for fast PDF processing",
        "inferenceSettings": {
            "temperature": 0.2,
            "top_p": 0.9,
            "top_k": 40,
            "max_tokens": 2048,
            "stream": True,
            "stop": []
        },
        "loadSettings": {
            "n_gpu_layers": -1,
            "n_batch": 512,
            "n_threads": 16,
            "n_ctx": 4096,
            "use_mmap": True,
            "use_mlock": False,
            "flash_attn": True,
            "cont_batching": True
        }
    }

    preset_path = preset_dir / "Performance_Optimized.preset.json"
    with open(preset_path, 'w', encoding='utf-8') as f:
        json.dump(optimized_preset, f, indent=2, ensure_ascii=False)

    print(f"✅ Created optimized preset: {preset_path}")

def main():
    print("🚀 LM Studio Optimizer")
    print("=" * 50)

    # Performance optimizations
    server_optimizations = {
        "gpu_layers": -1,
        "batch_size": 512,
        "thread_count": 16,
        "context_length": 4096,
        "use_flash_attention": True,
        "use_memory_mapping": True,
        "continuous_batching": True
    }

    inference_optimizations = {
        "temperature": 0.2,
        "top_p": 0.9,
        "top_k": 40,
        "max_tokens": 2048,
        "stream": True
    }

    # Find config files
    config_files = find_lm_studio_configs()
    print(f"📁 Found {len(config_files)} config files")

    modified_files = 0

    # Process each config file
    for config_path in config_files:
        if "http-server-config" in str(config_path):
            if optimize_config(config_path, server_optimizations):
                modified_files += 1
        elif "conversation-config" in str(config_path):
            if optimize_config(config_path, inference_optimizations):
                modified_files += 1
        elif "default-config" in str(config_path):
            # Model-specific configs
            combined_opts = {**server_optimizations, **inference_optimizations}
            if optimize_config(config_path, combined_opts):
                modified_files += 1

    # Create optimized preset
    create_optimized_preset()

    print("\n🎯 Optimization Summary:")
    print(f"   Modified {modified_files} config files")
    print("   Created optimized preset")
    print("\n💡 Next Steps:")
    print("   1. Restart LM Studio")
    print("   2. Load the 'Performance Optimized' preset")
    print("   3. Ensure GPU acceleration is enabled")
    print("   4. Test with convert_fast.py")

if __name__ == "__main__":
    main()
