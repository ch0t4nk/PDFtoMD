# LM Studio Configuration File Locator and Editor
# This script helps find and modify LM Studio configuration files

import os
import json
import glob
from pathlib import Path

def find_lm_studio_configs():
    """Find LM Studio configuration files"""
    print("🔍 Searching for LM Studio configuration files...")
    
    # Common LM Studio config locations
    possible_paths = [
        os.path.expanduser("~/.lmstudio"),
        os.path.expanduser("~/AppData/Roaming/lmstudio"),
        os.path.expanduser("~/AppData/Local/lmstudio"),
        "C:/Users/*/AppData/Roaming/lmstudio",
        "C:/Users/*/AppData/Local/lmstudio",
        "C:/Program Files/LM Studio",
        "C:/Program Files (x86)/LM Studio",
    ]
    
    found_configs = []
    
    for path_pattern in possible_paths:
        if "*" in path_pattern:
            # Handle wildcard paths
            for path in glob.glob(path_pattern):
                if os.path.exists(path):
                    found_configs.extend(search_config_files(path))
        else:
            if os.path.exists(path_pattern):
                found_configs.extend(search_config_files(path_pattern))
    
    return found_configs

def search_config_files(directory):
    """Search for configuration files in a directory"""
    config_files = []
    
    if not os.path.exists(directory):
        return config_files
    
    # Look for various config file types
    patterns = [
        "*.json",
        "*.yaml", 
        "*.yml",
        "*.toml",
        "*.ini",
        "*.cfg",
        "*config*",
        "*settings*",
        "*preferences*"
    ]
    
    for pattern in patterns:
        try:
            files = glob.glob(os.path.join(directory, "**", pattern), recursive=True)
            for file in files:
                if os.path.isfile(file):
                    config_files.append(file)
        except Exception:
            continue
    
    return config_files

def analyze_config_file(filepath):
    """Analyze a configuration file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse as JSON
        if filepath.endswith('.json'):
            try:
                data = json.loads(content)
                return analyze_json_config(data)
            except json.JSONDecodeError:
                pass
        
        # Look for performance-related keywords
        performance_keywords = [
            'gpu', 'batch', 'thread', 'context', 'token', 
            'temperature', 'layers', 'memory', 'cache',
            'acceleration', 'quantization', 'precision'
        ]
        
        found_settings = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            for keyword in performance_keywords:
                if keyword in line_lower and ('=' in line or ':' in line):
                    found_settings.append({
                        'line': i + 1,
                        'content': line.strip(),
                        'keyword': keyword
                    })
        
        return found_settings
        
    except Exception as e:
        return [{'error': str(e)}]

def analyze_json_config(data, path=""):
    """Analyze JSON configuration data"""
    settings = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            
            # Check if this looks like a performance setting
            key_lower = key.lower()
            performance_keys = [
                'gpu', 'batch', 'thread', 'context', 'token',
                'temperature', 'layers', 'memory', 'cache',
                'n_gpu_layers', 'n_batch', 'n_threads', 'n_ctx'
            ]
            
            if any(perf_key in key_lower for perf_key in performance_keys):
                settings.append({
                    'path': current_path,
                    'key': key,
                    'value': value,
                    'type': type(value).__name__
                })
            
            # Recurse into nested objects
            if isinstance(value, (dict, list)):
                settings.extend(analyze_json_config(value, current_path))
    
    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_path = f"{path}[{i}]"
            if isinstance(item, (dict, list)):
                settings.extend(analyze_json_config(item, current_path))
    
    return settings

def create_lm_studio_optimization_guide():
    """Create a comprehensive optimization guide"""
    guide = """
# LM Studio Optimization Guide

## 🎯 Performance Settings to Look For

### In LM Studio GUI:
1. **Model Loading Screen:**
   - Context Length: 4096 (not 8192+)
   - GPU Layers: -1 or "All" 
   - Quantization: Q4_K_M or Q5_K_M

2. **Chat/Playground Settings:**
   - Temperature: 0.1-0.3
   - Max Tokens: 2048-4096
   - Top P: 0.9
   - Top K: 40

3. **Advanced/Developer Settings:**
   - Batch Size: 512-1024
   - Thread Count: 8-16
   - Flash Attention: Enable
   - Memory Mapping: Enable

### Registry/Config File Settings:
If you find config files, look for these keys:

```json
{
  "n_gpu_layers": -1,
  "n_batch": 512,
  "n_threads": 16,
  "n_ctx": 4096,
  "temperature": 0.2,
  "top_p": 0.9,
  "top_k": 40,
  "use_mmap": true,
  "use_mlock": false,
  "flash_attn": true
}
```

## 🚀 Windows Performance Tweaks

### Power Settings:
```batch
powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c
```

### NVIDIA Settings:
- Open NVIDIA Control Panel
- Manage 3D Settings → Global Settings
- Power management mode: "Prefer maximum performance"
- CUDA - GPUs used by PhysX: Your RTX 4080

### Memory Settings:
- Virtual Memory: Set to system managed
- Disable Windows Search indexing on SSD
- Close unnecessary startup programs

## 📊 Monitoring Performance

### Check GPU Usage:
```
nvidia-smi -l 1
```

### Expected Performance:
- GPU Utilization: 85-95% during processing
- VRAM Usage: 7-8GB for Qwen2-VL-7B
- Processing Speed: 2-5 seconds per page
- Temperature: GPU should stay under 80°C
"""
    
    try:
        with open('LM_Studio_Optimization_Guide.md', 'w', encoding='utf-8') as f:
            f.write(guide)
        print("✅ Created LM_Studio_Optimization_Guide.md")
        return True
    except Exception as e:
        print(f"❌ Error creating guide: {e}")
        return False

def main():
    print("🔧 LM Studio Configuration Finder")
    print("=" * 40)
    
    # Find config files
    configs = find_lm_studio_configs()
    
    if configs:
        print(f"📁 Found {len(configs)} configuration files:")
        
        performance_configs = []
        
        for config in configs:
            print(f"\n📄 {config}")
            settings = analyze_config_file(config)
            
            if settings and not any('error' in s for s in settings):
                print(f"   ⚙️  Found {len(settings)} performance-related settings")
                performance_configs.append((config, settings))
                
                # Show first few settings
                for setting in settings[:3]:
                    if 'path' in setting:
                        print(f"      • {setting['path']}: {setting['value']}")
                    elif 'content' in setting:
                        print(f"      • Line {setting['line']}: {setting['content'][:50]}...")
            else:
                print("   ℹ️  No obvious performance settings found")
        
        if performance_configs:
            print(f"\n🎯 Found performance settings in {len(performance_configs)} files")
            print("   Manual editing may be required for optimization")
        
    else:
        print("❌ No LM Studio configuration files found")
        print("   LM Studio may store settings in registry or hidden locations")
    
    # Create optimization guide
    print(f"\n📚 Creating optimization guide...")
    create_lm_studio_optimization_guide()
    
    print(f"\n💡 Recommendations:")
    print("   1. Check LM Studio GUI settings manually")
    print("   2. Use .env.optimized for application settings")
    print("   3. Apply Windows power optimizations")
    print("   4. Monitor GPU usage during processing")
    print("   5. Test with convert_fast.py after changes")

if __name__ == "__main__":
    main()
