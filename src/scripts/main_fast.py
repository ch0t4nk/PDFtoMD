# Fast version of main.py with optimized settings for speed

import logging
import os
import shutil
import sys
import time

from dotenv import load_dotenv

from core import LLMClient
from core.FileWorker import create_worker
from core.Util import remove_markdown_warp

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)
logger = logging.getLogger(__name__)

load_dotenv()


def completion_fast(
    message,
    model="",
    system_prompt="",
    image_paths=None,
    temperature=0.1,  # Lower for speed
    max_tokens=4096,  # Reduced for speed
    retry_times=3,
):
    """Fast completion with optimized settings"""

    # Get API key and API base URL from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("Please set the OPENAI_API_KEY environment variables")
        exit(1)
    base_url = os.getenv("OPENAI_API_BASE")
    if not base_url:
        base_url = "https://api.openai.com/v1/"

    # If no model is specified, use the default model
    if not model:
        model = os.getenv("OPENAI_DEFAULT_MODEL")
        if not model:
            model = "gpt-4o"

    # Initialize LLMClient
    client = LLMClient.LLMClient(base_url=base_url, api_key=api_key, model=model)
    # Call completion method with retry mechanism
    for _ in range(retry_times):
        try:
            response = client.completion(
                user_message=message,
                system_prompt=system_prompt,
                image_paths=image_paths,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response
        except Exception as e:
            logger.error(f"LLM call failed: {str(e)}")
            # If retry fails, wait for a while before retrying
            time.sleep(0.3)  # Reduced retry delay
    return ""


def convert_image_to_markdown_fast(image_path):
    """Fast image conversion with shorter prompt"""
    system_prompt = """Convert this image to Markdown. Output only Markdown text content, no image references."""
    
    user_prompt = """Convert this document page to Markdown format:
1. Extract all text, headings, tables
2. Use proper Markdown syntax  
3. Include technical symbols and formulas
4. DO NOT include any image references like ![](filename.png)
5. Describe diagrams and images in text instead
6. Output Markdown only, no code blocks"""

    response = completion_fast(
        message=user_prompt,
        system_prompt=system_prompt,
        image_paths=[image_path],
        temperature=0.1,  # Lower for consistency and speed
        max_tokens=4096,  # Reduced for speed
    )
    response = remove_markdown_warp(response, "markdown")
    return response


def clean_non_existent_image_references(markdown_content):
    """Remove image references that point to non-existent files"""
    import re
    
    # Pattern to match markdown image references: ![alt text](filename)
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    def check_image_exists(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # Skip if it's already a proper relative path to our images directory
        if image_path.startswith('images/'):
            return match.group(0)  # Keep it
        
        # Skip if it's a web URL
        if image_path.startswith(('http://', 'https://', 'www.')):
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
    cleaned_content = re.sub(r'\n\n\n+', '\n\n', cleaned_content)
    
    return cleaned_content


if __name__ == "__main__":
    # Get configuration from environment variables set by convert_fast.py
    output_filename = os.environ.get('MARKPDF_OUTPUT_FILE', 'output.md')
    
    start_page = 1
    end_page = 0
    if len(sys.argv) > 2:
        start_page = int(sys.argv[1])
        end_page = int(sys.argv[2])
    elif len(sys.argv) > 1:
        start_page = 1
        end_page = int(sys.argv[1])

    # Read binary data from standard input
    input_data = sys.stdin.buffer.read()
    if not input_data:
        logger.error("No input data received")
        logger.error(
            "Usage: python main_fast.py [start_page] [end_page] < path_to_input.pdf"
        )
        exit(1)

    # Create output directory
    output_dir = f"output/{time.strftime('%Y%m%d%H%M%S')}_fast"
    os.makedirs(output_dir, exist_ok=True)

    # File type detection (same as original)
    input_filename = os.path.basename(sys.stdin.buffer.name)
    input_ext = os.path.splitext(input_filename)[1]

    if not input_ext or input_filename == "<stdin>":
        if input_data.startswith(b"%PDF-"):
            input_ext = ".pdf"
            logger.info("Recognized as PDF file by file content")
        elif input_data.startswith(b"\xff\xd8\xff\xdb"):
            input_ext = ".jpeg"
            logger.info("Recognized as JPEG file by file content")
        elif input_data.startswith(b"\xff\xd8\xff\xe0"):
            input_ext = ".jpg"
            logger.info("Recognized as JPG file by file content")
        elif input_data.startswith(b"\x89\x50\x4e\x47"):
            input_ext = ".png"
            logger.info("Recognized as PNG file by file content")
        elif input_data.startswith(b"\x42\x4d"):
            input_ext = ".bmp"
            logger.info("Recognized as BMP file by file content")
        else:
            logger.error("Unsupported file type")
            exit(1)

    input_path = os.path.join(output_dir, f"input{input_ext}")
    with open(input_path, "wb") as f:
        f.write(input_data)

    # create file worker
    try:
        worker = create_worker(input_path, start_page, end_page)
    except ValueError as e:
        logger.error(str(e))
        exit(1)

    # convert to images
    img_paths = worker.convert_to_images()
    logger.info("Image conversion completed")

    # convert to markdown with progress tracking
    markdown = ""
    total_pages = len(img_paths)
    
    # Collect processing metadata
    processing_start_time = time.time()
    page_times = []
    total_content_length = 0
    cleaned_images_count = 0
    
    for i, img_path in enumerate(sorted(img_paths), 1):
        img_path = img_path.replace("\\", "/")
        logger.info(f"Converting page {i}/{total_pages}: {os.path.basename(img_path)}")
        
        page_start_time = time.time()
        content = convert_image_to_markdown_fast(img_path)
        page_end_time = time.time()
        
        page_duration = page_end_time - page_start_time
        page_times.append(page_duration)
        
        if content:
            # Clean up non-existent image references from LLM-generated content
            original_content_length = len(content)
            content = clean_non_existent_image_references(content)
            if len(content) < original_content_length:
                cleaned_images_count += 1
            
            total_content_length += len(content)
            
            # Don't copy page screenshots - we only need the markdown content
            # Page screenshots (page_0001.jpg) are just temporary files for LLM processing
            
            # Write individual page file to temp directory (will be cleaned up)
            page_md_file = os.path.join(output_dir, f"page_{i:04d}.md")
            with open(page_md_file, "w", encoding="utf-8") as f:
                f.write(f"# Page {i}\n\n")
                f.write(content)
            
            # Add page to combined markdown without page image reference
            markdown += f"---\n# Page {i}\n---\n\n"
            markdown += content
            markdown += "\n\n"
            
            logger.info(f"Page {i} completed in {page_duration:.1f}s")
    
    processing_end_time = time.time()
    total_processing_time = processing_end_time - processing_start_time
    
    # Add processing metadata to the end of the markdown
    avg_page_time = sum(page_times) / len(page_times) if page_times else 0
    fastest_page = min(page_times) if page_times else 0
    slowest_page = max(page_times) if page_times else 0
    
    metadata = f"""---

## Processing Metadata

- **Total Pages:** {total_pages}
- **Processing Time:** {total_processing_time:.1f}s
- **Average Page Time:** {avg_page_time:.1f}s
- **Fastest Page:** {fastest_page:.1f}s
- **Slowest Page:** {slowest_page:.1f}s
- **Content Length:** {total_content_length:,} characters
- **Pages with Cleaned Images:** {cleaned_images_count}
- **Processed:** {time.strftime('%Y-%m-%d %H:%M:%S')}

"""
    
    markdown += metadata

    # Output Markdown to stdout for convert_fast.py
    # Use sys.stdout.buffer.write to handle Unicode properly
    try:
        sys.stdout.buffer.write(markdown.encode('utf-8'))
    except (UnicodeEncodeError, AttributeError):
        # Fallback: write to stderr log only
        logger.info("Unicode encoding issue - markdown saved to files only")
    
    logger.info("Fast conversion completed")
    logger.info(f"Processing completed in {total_processing_time:.1f}s (avg: {avg_page_time:.1f}s/page)")
    logger.info("No page images saved - only markdown content extracted")
    
    # Clean up temporary output directory after copying images
    try:
        if os.path.exists(output_dir):
            temp_files_count = len([f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))])
            shutil.rmtree(output_dir)
            logger.info(f"Temporary files cleaned up ({temp_files_count} files removed)")
    except Exception as e:
        logger.warning(f"Could not clean up temporary files: {e}")
    
    exit(0)
