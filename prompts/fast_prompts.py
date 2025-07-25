"""
Centralized Fast Processing Prompts for PDFtoMD
Single Source of Truth (SSOT) for all fast/main_fast.py prompts

Enterprise Enhancement for PDFtoMD
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0
"""

# =================================================================================
# FAST PROCESSING PROMPTS - Speed-Optimized, Lower Token Usage
# =================================================================================

FAST_SYSTEM_PROMPT = """Convert this image to Markdown. Output only Markdown text content, no image references."""

FAST_USER_PROMPT = """Convert this document page to Markdown format:
1. Extract all text, headings, tables
2. Use proper Markdown syntax
3. Include technical symbols and formulas
4. DO NOT include any image references like ![](filename.png)
5. Describe diagrams and images in text instead
6. Output Markdown only, no code blocks"""

# =================================================================================
# FAST PROCESSING SETTINGS
# =================================================================================

FAST_TEMPERATURE = 0.1    # Lower for consistency and speed
FAST_MAX_TOKENS = 4096    # Reduced for speed
FAST_MODEL_FALLBACK = "gpt-4o"  # Fallback if config model not available
