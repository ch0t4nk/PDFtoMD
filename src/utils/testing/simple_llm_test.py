# Simple LLM Test

import importlib.util
from pathlib import Path

# Import config using relative path - SSOT handles all environment loading
current_dir = Path(__file__).parent
root_dir = current_dir.parent.parent.parent  # Go up three levels from src/utils/testing/
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


def test_llm_simple():
    try:
        from core.LLMClient import LLMClient

        # Get config
        api_key = config.OPENAI_API_KEY
        base_url = config.OPENAI_API_BASE
        model = config.OPENAI_DEFAULT_MODEL

        print("🔧 Testing LLM Connection")
        print(f"Base URL: {base_url}")
        print(f"Model: {model}")
        print("-" * 40)

        # Initialize client
        client = LLMClient(base_url=base_url, api_key=api_key, model=model)
        print("✅ Client initialized")

        # Test simple completion
        response = client.completion(
            user_message="Hello! Please respond with just 'Test successful!'",
            temperature=0.1,
            max_tokens=50,
        )

        print(f"🤖 Response: {response}")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_llm_simple()
