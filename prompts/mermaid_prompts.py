"""
Centralized Mermaid-Enhanced Processing Prompts for PDFtoMD
Single Source of Truth (SSOT) for all Mermaid-enhanced API prompts

Enterprise Enhancement for PDFtoMD
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0
"""

# =================================================================================
# MERMAID-ENHANCED PROMPTS - High Quality with Visual Diagram Support
# =================================================================================

MERMAID_SYSTEM_PROMPT = """You are an expert document conversion assistant with advanced Mermaid diagram capabilities. Convert this document page to clean, professional Markdown format with integrated Mermaid diagrams where appropriate. Focus on accurate text extraction, proper structure, and visual diagram generation while maintaining readability."""

MERMAID_USER_PROMPT = """Convert this document page to Markdown format with these specific requirements:

1. **Text Extraction**: Extract ALL text accurately, including headers, body text, captions, and technical specifications
2. **Structure**: Use proper Markdown heading hierarchy (# ## ### etc.) based on document structure
3. **Tables**: Convert tables to proper Markdown table format with | separators
4. **Technical Content**: Preserve technical symbols, formulas, part numbers, and specifications exactly
5. **Code/Commands**: Use proper code blocks for any code examples or commands
6. **Lists**: Convert bulleted and numbered lists to proper Markdown list format
7. **No Image References**: DO NOT include any ![](filename.png) image references
8. **Describe Visuals**: Describe diagrams, schematics, and images in plain text
9. **Clean Output**: Output ONLY the Markdown content, no code block wrappers, no "```markdown"

Focus on creating clean, professional documentation that preserves all information from the original page."""

# =================================================================================
# MERMAID PROCESSING SETTINGS
# =================================================================================

MERMAID_TEMPERATURE = 0.05  # Very low for consistency
MERMAID_MAX_TOKENS = 8192  # Higher for complete conversion with diagrams
MERMAID_MODEL_FALLBACK = "gpt-4o"  # Fallback if config model not available
