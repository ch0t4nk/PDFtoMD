# Simple LLM Test

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
import os
from config import config

load_dotenv()

def test_llm_simple():
    try:
        from core.LLMClient import LLMClient
        
        # Get config
        api_key = config.OPENAI_API_KEY
        base_url = config.OPENAI_API_BASE
        model = config.OPENAI_DEFAULT_MODEL
        
        print(f"🔧 Testing LLM Connection")
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
            max_tokens=50
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