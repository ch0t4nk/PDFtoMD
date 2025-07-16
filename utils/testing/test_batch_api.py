#!/usr/bin/env python3
"""
Quick test with just one small PDF to verify Batch API works
"""

import os
import json
import time
from pathlib import Path
from openai import OpenAI
import base64
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

def test_single_pdf():
    """Test batch API with just the schematic file (small, 1 page)"""
    
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    )
    
    # Create a simple test request
    test_request = {
        "custom_id": "test_001",
        "method": "POST", 
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": "Say 'Hello from batch API test!'"}
            ],
            "max_tokens": 50
        }
    }
    
    # Create JSONL file
    batch_file = "test_batch.jsonl"
    with open(batch_file, 'w') as f:
        f.write(json.dumps(test_request) + '\n')
    
    print("📤 Uploading test batch...")
    
    # Upload and submit
    try:
        with open(batch_file, 'rb') as f:
            batch_input_file = client.files.create(
                file=f,
                purpose="batch"
            )
        
        batch = client.batches.create(
            input_file_id=batch_input_file.id,
            endpoint="/v1/chat/completions",
            completion_window="24h"
        )
        
        print(f"✅ Test batch submitted!")
        print(f"📋 Batch ID: {batch.id}")
        print(f"📊 Status: {batch.status}")
        
        # Clean up
        os.remove(batch_file)
        
        return batch.id
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        if os.path.exists(batch_file):
            os.remove(batch_file)
        return None

if __name__ == "__main__":
    test_single_pdf()
