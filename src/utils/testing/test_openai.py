#!/usr/bin/env python3
"""
OpenAI API Test - Check if your credits work
"""

import importlib.util
from pathlib import Path

from openai import OpenAI

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


def test_openai_api():
    """Test OpenAI API connection and credits"""

    api_key = config.OPENAI_API_KEY
    if not api_key:
        print("❌ No OPENAI_API_KEY found in .env file")
        return False

    try:
        client = OpenAI(api_key=api_key)

        # Simple test call
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cheapest option
            messages=[
                {
                    "role": "user",
                    "content": "Say 'Hello from OpenAI!' in exactly 5 words.",
                }
            ],
            max_tokens=20,
        )

        result = response.choices[0].message.content
        print("✅ OpenAI API working!")
        print(f"📝 Response: {result}")
        if response.usage:
            print(f"💰 Tokens used: {response.usage.total_tokens}")

        return True

    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        if "insufficient_quota" in str(e):
            print("💳 No credits remaining - you'll need to add payment method")
        elif "invalid_api_key" in str(e):
            print("🔑 Invalid API key - check your .env file")
        return False


if __name__ == "__main__":
    print("🧪 Testing OpenAI API Connection")
    print("=" * 40)
    test_openai_api()
