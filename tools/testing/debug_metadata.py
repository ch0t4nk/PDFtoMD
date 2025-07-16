#!/usr/bin/env python3
"""
Debug metadata embedding
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.metadata_embedder import MetadataEmbedder

def debug_embedding():
    """Debug the metadata embedding process"""

    # Create test file
    test_file = Path("outputs/converted/debug_test.md")
    test_file.parent.mkdir(parents=True, exist_ok=True)

    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("# Debug Test\n\nThis is a test file for debugging metadata embedding.\n")

    print(f"✓ Created test file: {test_file}")

    # Test the embedder
    embedder = MetadataEmbedder()
    embedder.session_id = 'debug_123'
    embedder.batch_id = 'batch_debug'
    embedder.total_cost = 0.050
    embedder.total_files = 1
    embedder.total_pages = 10
    embedder.linting_stats = {'fixes': 5, 'size_reduction': 1000}

    # File data for this test
    file_data = {
        'debug_test': {  # Remove .md extension for lookup
            'source_pdf': 'debug_test.pdf',
            'pages': 10,
            'cost': 0.050,
            'cost_per_page': 0.005,
            'tokens': 2000
        }
    }

    print(f"📝 Adding metadata to: {test_file}")
    success = embedder.add_file_metadata(str(test_file), file_data)
    print(f"✓ Metadata added: {success}")

    # Read the result
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print("\n📄 Enhanced file content:")
    print("="*60)
    print(content[:500] + "..." if len(content) > 500 else content)
    print("="*60)

if __name__ == "__main__":
    debug_embedding()
