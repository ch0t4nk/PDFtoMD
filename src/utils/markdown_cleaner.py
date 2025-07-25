#!/usr/bin/env python3
"""
Centralized Markdown Cleaning Utilities for PDFtoMD
Consolidates markdown processing functions from across the codebase

Enterprise Enhancement for PDFtoMD
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

This module centralizes markdown cleaning functionality that was previously
duplicated across main.py, main_fast.py, and other files.

Author: Joseph Wright (github: ch0t4nk)
Created: July 25, 2025
Version: 1.0
"""

import os
import re
import logging

logger = logging.getLogger(__name__)


def clean_non_existent_image_references(markdown_content):
    """
    Remove image references that point to non-existent files
    Consolidated from main_fast.py and main.py
    """
    # Pattern to match markdown image references: ![alt text](filename)
    image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"

    def check_image_exists(match):
        alt_text = match.group(1)
        image_path = match.group(2)

        # Skip if it's already a proper relative path to our images directory
        if image_path.startswith("images/"):
            return match.group(0)  # Keep it

        # Skip if it's a web URL
        if image_path.startswith(("http://", "https://", "www.")):
            return match.group(0)  # Keep it

        # For local file references that don't exist, replace with text
        if not os.path.exists(image_path):
            logger.info(f"Removing non-existent image reference: {image_path}")
            # Return just the alt text if it's meaningful, otherwise remove entirely
            if alt_text and len(alt_text.strip()) > 0:
                return f"**{alt_text}**"  # Convert to bold text
            else:
                return ""  # Remove entirely

        return match.group(0)  # Keep existing image if file exists

    # Replace all image references
    cleaned_content = re.sub(image_pattern, check_image_exists, markdown_content)

    # Clean up any double newlines that might result from removed images
    cleaned_content = re.sub(r"\n\n\n+", "\n\n", cleaned_content)

    return cleaned_content


def remove_markdown_warp(content):
    """
    Remove markdown code block wrappers from content
    Enhanced version of function from Util.py
    """
    if not content:
        return content
    
    # Remove markdown code block markers
    content = content.strip()
    
    # Remove starting ```markdown or ``` 
    if content.startswith("```markdown"):
        content = content[11:].strip()
    elif content.startswith("```"):
        content = content[3:].strip()
    
    # Remove ending ```
    if content.endswith("```"):
        content = content[:-3].strip()
    
    return content


def clean_markdown_formatting(content):
    """
    Clean up various markdown formatting issues
    New centralized function for comprehensive markdown cleanup
    """
    if not content:
        return content
    
    # Remove markdown wrappers
    content = remove_markdown_warp(content)
    
    # Clean up image references
    content = clean_non_existent_image_references(content)
    
    # Fix excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Fix trailing whitespace on lines
    content = re.sub(r' +$', '', content, flags=re.MULTILINE)
    
    # Ensure single space after list markers
    content = re.sub(r'^(\s*[-*+])\s+', r'\1 ', content, flags=re.MULTILINE)
    content = re.sub(r'^(\s*\d+\.)\s+', r'\1 ', content, flags=re.MULTILINE)
    
    # Fix spacing around headers
    content = re.sub(r'\n(#{1,6})', r'\n\n\1', content)
    content = re.sub(r'(#{1,6}.*)\n([^\n#])', r'\1\n\n\2', content)
    
    # Clean up multiple spaces in content
    content = re.sub(r'  +', ' ', content)
    
    # Ensure file ends with single newline
    content = content.rstrip() + '\n'
    
    return content


def extract_alt_text_from_images(content):
    """
    Extract alt text from image references for accessibility
    Useful for processing image-heavy documents
    """
    image_pattern = r"!\[([^\]]*)\]\([^)]+\)"
    alt_texts = re.findall(image_pattern, content)
    return [alt.strip() for alt in alt_texts if alt.strip()]


def convert_images_to_descriptions(content):
    """
    Convert image references to descriptive text
    Useful for text-only outputs
    """
    def replace_image_with_description(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        if alt_text and alt_text.strip():
            return f"[Image: {alt_text.strip()}]"
        else:
            image_name = os.path.basename(image_path)
            return f"[Image: {image_name}]"
    
    image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    return re.sub(image_pattern, replace_image_with_description, content)


def normalize_line_endings(content):
    """
    Normalize line endings to Unix-style (LF)
    """
    return content.replace('\r\n', '\n').replace('\r', '\n')


def main():
    """Main entry point for standalone testing"""
    import sys
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if os.path.exists(input_file):
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print("Original content length:", len(content))
            
            cleaned = clean_markdown_formatting(content)
            
            print("Cleaned content length:", len(cleaned))
            print("Image alt texts found:", extract_alt_text_from_images(content))
            
            # Write cleaned version
            output_file = input_file.replace('.md', '_cleaned.md')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            
            print(f"Cleaned version saved to: {output_file}")
        else:
            print(f"File not found: {input_file}")
    else:
        print("Usage: python markdown_cleaner.py <markdown_file>")


if __name__ == "__main__":
    main()
