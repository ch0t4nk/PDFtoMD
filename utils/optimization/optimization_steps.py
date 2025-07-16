#!/usr/bin/env python3
"""
Optimization Steps Reminder
Shows you exactly what to do next for optimal performance
"""

print("🚀 LM Studio Optimization - Next Steps")
print("=" * 50)
print()

print("1. 🔄 RESTART LM Studio (Required)")
print("   - Close LM Studio completely")
print("   - Restart the application")
print("   - This loads the new configuration files")
print()

print("2. ⚙️  Check Settings in LM Studio GUI")
print("   - Load your Qwen2-VL-7B-Instruct model")
print("   - In model loading screen, verify:")
print("     • Context Length: 4096 (not higher)")
print("     • GPU Layers: All (-1)")
print("     • Batch Size: 512-1024 if visible")
print()

print("3. 🎮 Load the Performance Preset")
print("   - Go to Chat/Playground")
print("   - Look for preset dropdown")
print("   - Select 'Performance Optimized' if available")
print()

print("4. 🧪 Test Performance")
print("   - Run: python test_optimized_performance.py")
print("   - This will measure your new speed")
print()

print("5. 📄 Process PDFs with Optimized Settings")
print("   - Run: python convert_fast.py")
print("   - Monitor GPU usage: nvidia-smi -l 1")
print()

print("📊 Expected Improvements:")
print("   - 3-10x faster processing")
print("   - 85-95% GPU utilization")
print("   - 2-5 seconds per PDF page")
print("   - More consistent performance")
print()

print("🔍 If Performance Doesn't Improve:")
print("   1. Check LM Studio server logs")
print("   2. Verify GPU drivers are up to date")
print("   3. Try different batch sizes (256, 512, 1024)")
print("   4. Ensure no other GPU-intensive apps are running")
print()

print("✨ Configuration Files Modified:")
print("   - C:\\Users\\joeyw\\.lmstudio\\.internal\\http-server-config.json")
print("   - C:\\Users\\joeyw\\.lmstudio\\.internal\\conversation-config.json")
print("   - Model-specific configs for all your models")
print("   - Created: Performance_Optimized.preset.json")
print()

print("💾 Backups Created:")
print("   - All original files backed up with .backup extension")
print("   - You can restore if needed")
