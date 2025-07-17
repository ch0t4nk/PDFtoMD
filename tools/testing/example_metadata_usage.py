#!/usr/bin/env python3
"""
Working Example: Complete Metadata Enhancement System

This script demonstrates how to use the enhanced metadata system
to add both embedded headers and session summaries to your conversions.

Example usage:
    python example_metadata_usage.py
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.metadata_embedder import enhance_converted_files


def demo_metadata_system():
    """Demonstrate the complete metadata system with realistic data"""

    # Example: Create some demo converted files
    converted_dir = Path("outputs/converted")
    converted_dir.mkdir(parents=True, exist_ok=True)

    # Sample converted files with content
    demo_files = {
        "20250716_dm00105823-nucleo-f401re-user-manual_batch.md": """# STM32 Nucleo-F401RE User Manual

## Overview
This document provides comprehensive information about the STM32 Nucleo-F401RE development board.

## Features
- STM32F401RET6 microcontroller
- Arduino Uno V3 connectivity
- ST morpho extension pin headers
- On-board ST-LINK/V2-1 debugger/programmer

## Getting Started
Follow these steps to begin developing with your Nucleo board...
""",
        "20250716_stsw-spin002_batch.md": """# STSW-SPIN002 Software Package

## Description
Motor control software package for STM32 microcontrollers.

## Components
- Motor control libraries
- Example applications
- Documentation

## Installation
Download and extract the package to your development environment.
""",
        "20250716_um1724-stm32-nucleo64-boards_batch.md": """# STM32 Nucleo-64 Boards User Manual

## Board Family Overview
The STM32 Nucleo-64 board family provides an affordable and flexible platform.

## Supported MCUs
- STM32F401RE
- STM32F411RE
- STM32F446RE
- And many more...

## Development Environment
Compatible with multiple IDEs and toolchains.
""",
    }

    # Create the demo files
    for filename, content in demo_files.items():
        file_path = converted_dir / filename
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ Created demo file: {filename}")

    # Realistic batch data from a conversion session
    batch_data = {
        "session_id": "20250716_143545",
        "batch_id": "batch_6877d5cf9db48190aff4f8e23e5e61c9",
        "total_cost": 1.1130,
        "total_files": 3,
        "total_pages": 186,
        "session_start": "2025-07-16 14:35:45",
        "session_end": "2025-07-16 14:42:18",
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
                "cost": 0.5544,
                "cost_per_page": 0.0061,
                "tokens": 3543901,
                "final_size": "127KB",
            },
        ],
    }

    # Linting statistics from post-processing
    linting_stats = {"fixes": 47, "size_reduction": 203847, "processing_time": 12.3}

    print("\n🚀 Enhancing converted files with metadata...")

    # Apply the metadata enhancement
    enhance_converted_files(str(converted_dir), batch_data, linting_stats)

    print("✅ Metadata enhancement completed!")
    print("\n📊 Results:")
    print(f"   - Enhanced {len(demo_files)} markdown files with embedded metadata")
    print("   - Created session summary in outputs/metadata/")
    print(f"   - Total batch cost: ${batch_data['total_cost']:.4f}")
    print(
        f"   - Average cost per page: ${batch_data['total_cost'] / batch_data['total_pages']:.4f}"
    )

    # Show what was created
    print("\n📁 Files enhanced:")
    for filename in demo_files.keys():
        print(f"   - {filename} (now includes conversion metadata)")

    # Check if summary was created
    metadata_dir = Path("outputs/metadata")
    if metadata_dir.exists():
        summaries = list(metadata_dir.glob("*_summary.md"))
        if summaries:
            print(f"\n📋 Session summary created: {summaries[0].name}")

    print("\n🎯 What you get:")
    print("   Option B ✓ - Each file has embedded metadata headers")
    print("   Option C ✓ - Standalone session summary for comparison")
    print("   🔒 Safety ✓ - Original PDFs never touched")


if __name__ == "__main__":
    demo_metadata_system()
