"""
Centralized Standard Processing Prompts for PDFtoMD
Single Source of Truth (SSOT) for all standard/main.py prompts

Enterprise Enhancement for PDFtoMD
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0
"""

# =================================================================================
# STANDARD PROCESSING PROMPTS - Balanced Quality and Performance
# =================================================================================

STANDARD_SYSTEM_PROMPT = """You are a helpful assistant that can convert images to Markdown format. You are given an image, and you need to convert it to Markdown format. Please output the Markdown content only, without any other text."""

STANDARD_USER_PROMPT = """Below is the image of one page of a document, please read the content in the image and transcribe it into plain Markdown format. Please note:
1. Identify heading levels, text styles, formulas, and the format of table rows and columns
2. Mathematical formulas should be transcribed using LaTeX syntax, ensuring consistency with the original
3. Please output the Markdown content only, without any other text.

Output Example:
```markdown
{example}
```"""

# =================================================================================
# STANDARD PROCESSING SETTINGS
# =================================================================================

STANDARD_TEMPERATURE = 0.3   # Balanced for quality and variation
STANDARD_MAX_TOKENS = 8192   # Generous limit for full pages
STANDARD_MODEL_FALLBACK = "gpt-4o"  # Fallback if config model not available
