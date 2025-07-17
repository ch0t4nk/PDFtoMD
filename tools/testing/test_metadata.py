#!/usr/bin/env python3
"""
Simple test for metadata embedding
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from utils.metadata_embedder import MetadataEmbedder


def test_metadata():
    print("🔧 Testing Metadata Header Creation...")

    embedder = MetadataEmbedder()
    embedder.session_id = "20250716_123456"
    embedder.batch_id = "batch_6877d5cf9db48190aff4f8e23e5e61c9"
    embedder.total_cost = 1.1130
    embedder.total_files = 4
    embedder.total_pages = 189
    embedder.linting_stats = {"fixes": 22, "size_reduction": 176683}

    # Test header creation
    file_info = {
        "source_pdf": "dm00105823-nucleo-f401re-user-manual.pdf",
        "pages": 91,
        "cost": 0.5359,
        "cost_per_page": 0.0059,
        "tokens": 3424316,
    }

    header = embedder._create_file_header(
        "20250716_dm00105823-nucleo-f401re-user-manual_batch.md", file_info
    )
    print("📝 Generated Header:")
    print(header)
    print("\n" + "=" * 60)

    # Create a session summary
    batch_data = {
        "session_id": "20250716_123456",
        "batch_id": "batch_6877d5cf9db48190aff4f8e23e5e61c9",
        "total_cost": 1.1130,
        "total_files": 4,
        "total_pages": 189,
        "files": [
            {
                "name": "dm00105823-nucleo-f401re-user-manual.pdf",
                "pages": 91,
                "cost": 0.5359,
                "cost_per_page": 0.0059,
                "tokens": 3424316,
                "final_size": "128KB",
            },
            {
                "name": "stsw-spin002.pdf",
                "pages": 4,
                "cost": 0.0227,
                "cost_per_page": 0.0057,
                "tokens": 149154,
                "final_size": "4KB",
            },
            {
                "name": "um1724-stm32-nucleo64-boards.pdf",
                "pages": 91,
                "cost": 0.5355,
                "cost_per_page": 0.0059,
                "tokens": 3423665,
                "final_size": "127KB",
            },
            {
                "name": "x-nucleo-ihm03a1_schematic.pdf",
                "pages": 3,
                "cost": 0.0189,
                "cost_per_page": 0.0063,
                "tokens": 115021,
                "final_size": "17KB",
            },
        ],
    }

    embedder.files_data = batch_data["files"]
    summary = embedder._generate_session_summary_content(batch_data)

    print("\n📊 Generated Session Summary Preview:")
    print(summary[:1000] + "..." if len(summary) > 1000 else summary)


if __name__ == "__main__":
    test_metadata()
