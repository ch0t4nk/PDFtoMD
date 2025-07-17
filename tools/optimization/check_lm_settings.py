# LM Studio Settings Checker and Optimizer
# This script checks current LM Studio settings and suggests optimizations

import sys
import time

import requests

LM_STUDIO_BASE = "http://192.168.56.1:1234"


def check_connection():
    """Check if LM Studio is accessible"""
    try:
        response = requests.get(f"{LM_STUDIO_BASE}/v1/models", timeout=5)
        if response.status_code == 200:
            print("✅ LM Studio connection successful")
            return True
        else:
            print(f"❌ LM Studio returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to LM Studio: {e}")
        return False


def get_model_info():
    """Get current loaded model information"""
    try:
        response = requests.get(f"{LM_STUDIO_BASE}/v1/models", timeout=5)
        if response.status_code == 200:
            models = response.json()
            print(f"\n📊 Available Models ({len(models['data'])} total):")
            for model in models["data"]:
                print(f"   🤖 {model['id']}")
            return models["data"]
        return []
    except Exception as e:
        print(f"❌ Error getting model info: {e}")
        return []


def test_completion_speed():
    """Test completion speed with current settings"""
    print("\n🧪 Testing completion speed...")

    test_payload = {
        "model": "Qwen2-VL-7B-Instruct",
        "messages": [{"role": "user", "content": "Say 'Hello World' exactly."}],
        "max_tokens": 10,
        "temperature": 0.1,
    }

    try:
        start_time = time.time()
        response = requests.post(
            f"{LM_STUDIO_BASE}/v1/chat/completions", json=test_payload, timeout=30
        )
        end_time = time.time()

        if response.status_code == 200:
            duration = end_time - start_time
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            print(f"✅ Test completed in {duration:.2f} seconds")
            print(f"📝 Response: {content}")
            return duration
        else:
            print(f"❌ Test failed with status {response.status_code}")
            print(f"Error: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Test error: {e}")
        return None


def test_vision_speed():
    """Test vision processing speed"""
    print("\n👁️ Testing vision processing speed...")

    # Use a small test image (we'll encode a simple base64 image)
    test_image_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=="

    test_payload = {
        "model": "Qwen2-VL-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What do you see?"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{test_image_b64}"},
                    },
                ],
            }
        ],
        "max_tokens": 50,
        "temperature": 0.1,
    }

    try:
        start_time = time.time()
        response = requests.post(
            f"{LM_STUDIO_BASE}/v1/chat/completions", json=test_payload, timeout=30
        )
        end_time = time.time()

        if response.status_code == 200:
            duration = end_time - start_time
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            print(f"✅ Vision test completed in {duration:.2f} seconds")
            print(f"📝 Response: {content[:100]}...")
            return duration
        else:
            print(f"❌ Vision test failed with status {response.status_code}")
            print(f"Error: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Vision test error: {e}")
        return None


def check_server_info():
    """Try to get server information"""
    print("\n🔍 Checking server information...")

    # Try different endpoints that might give us info
    endpoints = [
        "/health",
        "/v1/completions",
        "/v1/embeddings",
        "/stats",
        "/info",
        "/status",
    ]

    for endpoint in endpoints:
        try:
            response = requests.get(f"{LM_STUDIO_BASE}{endpoint}", timeout=5)
            if response.status_code == 200:
                print(f"✅ {endpoint}: Available")
                if endpoint == "/stats":
                    print(f"   Data: {response.text[:200]}...")
            elif response.status_code == 404:
                print(f"❌ {endpoint}: Not found")
            else:
                print(f"⚠️  {endpoint}: Status {response.status_code}")
        except Exception as e:
            print(f"❌ {endpoint}: Error - {e}")


def benchmark_different_settings():
    """Test with different parameter settings to find optimal"""
    print("\n⚡ Benchmarking different settings...")

    test_configs = [
        {"max_tokens": 50, "temperature": 0.1, "name": "Fast & Focused"},
        {"max_tokens": 100, "temperature": 0.1, "name": "Medium & Focused"},
        {"max_tokens": 50, "temperature": 0.3, "name": "Fast & Creative"},
        {"max_tokens": 200, "temperature": 0.1, "name": "Long & Focused"},
    ]

    results = []

    for config in test_configs:
        print(f"\n🧪 Testing: {config['name']}")

        test_payload = {
            "model": "Qwen2-VL-7B-Instruct",
            "messages": [
                {
                    "role": "user",
                    "content": "Describe the color blue in technical terms.",
                }
            ],
            "max_tokens": config["max_tokens"],
            "temperature": config["temperature"],
        }

        try:
            start_time = time.time()
            response = requests.post(
                f"{LM_STUDIO_BASE}/v1/chat/completions", json=test_payload, timeout=60
            )
            end_time = time.time()

            if response.status_code == 200:
                duration = end_time - start_time
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                tokens_generated = len(content.split())

                print(f"   ⏱️  Duration: {duration:.2f}s")
                print(f"   📊 Tokens: ~{tokens_generated}")
                print(f"   🚀 Speed: {tokens_generated / duration:.1f} tokens/sec")

                results.append(
                    {
                        "config": config["name"],
                        "duration": duration,
                        "tokens": tokens_generated,
                        "speed": tokens_generated / duration,
                    }
                )
            else:
                print(f"   ❌ Failed: {response.status_code}")

        except Exception as e:
            print(f"   ❌ Error: {e}")

    if results:
        print("\n🏆 Benchmark Results:")
        results.sort(key=lambda x: x["speed"], reverse=True)
        for i, result in enumerate(results, 1):
            print(
                f"   {i}. {result['config']}: {result['speed']:.1f} tokens/sec ({result['duration']:.2f}s)"
            )


def generate_optimization_report():
    """Generate a comprehensive optimization report"""
    print("\n📋 OPTIMIZATION RECOMMENDATIONS:")
    print("=" * 50)

    print("🔧 LM Studio GUI Settings to Check:")
    print("   1. Model Tab → Advanced Settings:")
    print("      - Context Length: Set to 4096 (not 8192+)")
    print("      - GPU Layers: Set to -1 or 99 (use all GPU)")
    print("      - Batch Size: Increase to 512-1024")
    print("   2. Settings → Hardware:")
    print("      - GPU Memory: Allocate 12-14GB")
    print("      - Keep CPU threads: 8-16")

    print("\n🖥️ System Optimizations:")
    print("   1. Windows Power Plan: High Performance")
    print("   2. NVIDIA Control Panel:")
    print("      - Power management: Prefer maximum performance")
    print("      - CUDA GPUs: Use GeForce RTX 4080")

    print("\n📱 Application Settings:")
    print("   1. Use max_tokens: 4096 (not 8192)")
    print("   2. Use temperature: 0.1-0.3 (not 0.5+)")
    print("   3. Reduce retry delays to 0.3s")

    print("\n🎯 Expected Performance:")
    print("   - Target: 2-5 seconds per page")
    print("   - Current Vision Model: Qwen2-VL-7B-Instruct")
    print("   - GPU Usage: Should be 90%+ during processing")


def main():
    print("🚀 LM Studio Settings Checker & Optimizer")
    print("=" * 50)

    # Basic connectivity check
    if not check_connection():
        print("\n❌ Cannot proceed without LM Studio connection")
        sys.exit(1)

    # Get model information
    models = get_model_info()

    # Check server endpoints
    check_server_info()

    # Test current performance
    text_speed = test_completion_speed()
    vision_speed = test_vision_speed()

    # Benchmark different settings
    benchmark_different_settings()

    # Generate optimization report
    generate_optimization_report()

    print("\n✅ Analysis complete!")
    if text_speed and vision_speed:
        print("📊 Current Performance Summary:")
        print(f"   - Text completion: {text_speed:.2f}s")
        print(f"   - Vision processing: {vision_speed:.2f}s")


if __name__ == "__main__":
    main()
