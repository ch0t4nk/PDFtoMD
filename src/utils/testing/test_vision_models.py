# Test Different Models for Vision Support

from dotenv import load_dotenv
import os
from core.LLMClient import LLMClient
import requests

load_dotenv()

def test_model_vision_support(model_name):
    """Test if a model supports vision by checking its capabilities"""

    try:
        base_url = os.getenv("OPENAI_API_BASE")
        api_key = os.getenv("OPENAI_API_KEY")

        print(f"🧪 Testing model: {model_name}")

        # Initialize client with the test model
        client = LLMClient(base_url=base_url, api_key=api_key, model=model_name)

        # Try a simple text completion first
        try:
            response = client.completion(
                user_message="Hello, can you see images?",
                max_tokens=20,
                temperature=0.1
            )
            print(f"✅ Text completion works: {response[:50]}...")

            # Now try with a dummy image path (this will fail but tell us if vision is supported)
            try:
                response = client.completion(
                    user_message="Describe this image",
                    image_paths=["tests/demo_01.png"],
                    max_tokens=20,
                    temperature=0.1
                )
                print(f"✅ Vision supported! Response: {response[:50]}...")
                return True
            except Exception as e:
                error_msg = str(e)
                if "does not support images" in error_msg:
                    print(f"❌ No vision support: {error_msg}")
                    return False
                else:
                    print(f"🔍 Other error (might still support vision): {error_msg}")
                    return None

        except Exception as e:
            print(f"❌ Text completion failed: {e}")
            return False

    except Exception as e:
        print(f"❌ Model initialization failed: {e}")
        return False

def main():
    # Available models from the earlier API call
    models_to_test = [
        "deepseek/deepseek-r1-0528-qwen3-8b",  # Current model
        "qwen/qwen3-32b",
        "microsoft/phi-4-reasoning-plus",
        "lmstudio-community/qwen3-30b-a3b",
        "unsloth/qwen3-30b-a3b",
        "deepseek-r1-distill-qwen-7b"
    ]

    print("🔍 Testing Models for Vision Support")
    print("=" * 50)

    vision_models = []
    text_only_models = []

    for model in models_to_test:
        result = test_model_vision_support(model)
        if result is True:
            vision_models.append(model)
        elif result is False:
            text_only_models.append(model)
        print("-" * 30)

    print("\n📊 Results Summary:")
    print(f"🖼️  Vision-capable models: {len(vision_models)}")
    for model in vision_models:
        print(f"   ✅ {model}")

    print(f"📝 Text-only models: {len(text_only_models)}")
    for model in text_only_models:
        print(f"   📝 {model}")

if __name__ == "__main__":
    main()
