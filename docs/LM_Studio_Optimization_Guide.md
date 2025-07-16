
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
