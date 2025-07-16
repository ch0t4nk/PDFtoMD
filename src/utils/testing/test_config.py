# Test Environment Configuration

import os
from dotenv import load_dotenv
import importlib.util
from pathlib import Path

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

def test_environment():
    """Test if environment variables are properly configured"""
    load_dotenv()

    api_key = config.OPENAI_API_KEY
    base_url = config.OPENAI_API_BASE
    model = config.OPENAI_DEFAULT_MODEL

    print("🔧 Environment Configuration Test")
    print("=" * 40)
    print(f"API Key: {api_key}")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")
    print("=" * 40)

    if all([api_key, base_url, model]):
        print("✅ All environment variables are set!")
        return True
    else:
        print("❌ Missing environment variables!")
        return False

if __name__ == "__main__":
    test_environment()