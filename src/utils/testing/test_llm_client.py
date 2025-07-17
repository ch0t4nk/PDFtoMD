# LLM Client Diagnostic Test

import importlib.util
import sys
from pathlib import Path

from dotenv import load_dotenv

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


def test_llm_client():
    """Test LLM client initialization and basic connectivity"""
    load_dotenv()

    print("🔧 LLM Client Diagnostic Test")
    print("=" * 50)

    try:
        # Import core modules
        from core.LLMClient import LLMClient

        print("✅ Successfully imported LLMClient")

        # Get configuration
        api_key = config.OPENAI_API_KEY
        base_url = config.OPENAI_API_BASE
        model = config.OPENAI_DEFAULT_MODEL

        if not all([api_key, base_url, model]):
            print("❌ Missing required environment variables")
            return False

        print(f"🔗 Base URL: {base_url}")
        print(f"🤖 Model: {model}")
        print(f"🔑 API Key: {api_key}")

        # Initialize client
        client = LLMClient(base_url=base_url, api_key=api_key, model=model)
        print("✅ LLM Client initialized successfully")

        # Test basic functionality with a simple prompt
        print("\n🧪 Testing simple completion...")
        try:
            response = client.completion(
                user_message="Hello! Please respond with just 'Test successful!'",
                temperature=0.1,
                max_tokens=50,
            )
            print(f"✅ LLM Response: {response}")
            return True
        except Exception as e:
            print(f"❌ LLM completion failed: {e}")
            return False

    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = test_llm_client()
    sys.exit(0 if success else 1)
