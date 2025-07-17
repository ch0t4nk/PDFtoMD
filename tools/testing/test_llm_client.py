# LLM Client Diagnostic Test

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from config import config

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
                max_tokens=50
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