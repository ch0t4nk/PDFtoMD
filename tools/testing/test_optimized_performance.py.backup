#!/usr/bin/env python3
"""
Performance Test for Optimized LM Studio Settings
Tests the speed improvements after configuration optimization
"""

import time
import requests
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def test_api_speed(prompt: str, description: str) -> float:
    """Test API response speed"""
    print(f"🧪 Testing: {description}")
    
    client = OpenAI(
        api_key="lm-studio",
        base_url=os.getenv("OPENAI_API_BASE", "http://192.168.56.1:1234/v1")
    )
    
    start_time = time.time()
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_DEFAULT_MODEL", "Qwen2-VL-7B-Instruct"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=100,
            stream=False
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Get response length
        response_text = response.choices[0].message.content or ""
        token_count = len(response_text.split())
        
        print(f"   ⏱️  {duration:.2f}s ({token_count} tokens)")
        print(f"   📝 '{response_text[:50]}{'...' if len(response_text) > 50 else ''}'")
        
        return duration
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return float('inf')

def test_gpu_status():
    """Check if GPU acceleration is working"""
    print("🖥️  Checking GPU Status:")
    
    try:
        import subprocess
        result = subprocess.run(['nvidia-smi', '--query-gpu=index,name,memory.used,memory.total,utilization.gpu', 
                               '--format=csv,noheader,nounits'], 
                               capture_output=True, text=True)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                parts = line.split(', ')
                if len(parts) >= 5:
                    gpu_id, name, mem_used, mem_total, util = parts
                    print(f"   GPU {gpu_id}: {name}")
                    print(f"   Memory: {mem_used}MB / {mem_total}MB")
                    print(f"   Utilization: {util}%")
        else:
            print("   ❌ nvidia-smi not available")
    
    except Exception as e:
        print(f"   ⚠️  Could not check GPU status: {e}")

def main():
    print("🚀 LM Studio Performance Test")
    print("=" * 50)
    
    # Check GPU first
    test_gpu_status()
    print()
    
    # Test different complexity levels
    tests = [
        ("Hello, how are you?", "Simple greeting"),
        ("What is the capital of France? Explain briefly.", "Factual question"),
        ("Describe how machine learning works in 2-3 sentences.", "Technical explanation"),
        ("Convert this text to markdown format: Hello World Title", "Format conversion")
    ]
    
    total_time = 0
    completed_tests = 0
    
    for prompt, description in tests:
        duration = test_api_speed(prompt, description)
        if duration != float('inf'):
            total_time += duration
            completed_tests += 1
        print()
    
    if completed_tests > 0:
        avg_time = total_time / completed_tests
        print(f"📊 Performance Summary:")
        print(f"   Average response time: {avg_time:.2f}s")
        print(f"   Completed tests: {completed_tests}/{len(tests)}")
        
        # Compare with baseline
        baseline = 0.64  # From previous tests
        if avg_time < baseline:
            improvement = ((baseline - avg_time) / baseline) * 100
            print(f"   🎉 {improvement:.1f}% faster than baseline!")
        else:
            print(f"   ⚠️  {avg_time/baseline:.1f}x slower than baseline")
    else:
        print("❌ No tests completed successfully")
    
    print("\n💡 Next steps:")
    print("   1. If performance improved: run convert_fast.py on PDFs")
    print("   2. If no improvement: restart LM Studio and try again")
    print("   3. Check GPU utilization during processing")

if __name__ == "__main__":
    main()
