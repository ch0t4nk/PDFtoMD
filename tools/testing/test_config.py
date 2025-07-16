# Test Environment Configuration

import os
from dotenv import load_dotenv

def test_environment():
    """Test if environment variables are properly configured"""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_API_BASE") 
    model = os.getenv("OPENAI_DEFAULT_MODEL")
    
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
