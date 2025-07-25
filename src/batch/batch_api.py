#!/usr/bin/env python3
"""
OpenAI Batch API PDF Converter
Efficiently process multiple PDFs using OpenAI's Batch API (50% cost reduction + better rate limits)

Enterprise Enhancement for PDFtoMD
Copyright (c) 2025 Joseph Wright (github: ch0t4nk)
Licensed under the Apache License, Version 2.0

This file is part of the enterprise enhancement suite for PDFtoMD,
providing efficient PDF processing using OpenAI's Batch API for significant
cost reduction and improved rate limit management.

Author: Joseph Wright (github: ch0t4nk)
Created: July 16, 2025
Version: 1.0
"""

import base64
import importlib.util
import json
import os
import shutil
import sys
import time
from pathlib import Path

from openai import OpenAI
import openai

# Import config using relative path
current_dir = Path(__file__).parent
root_dir = current_dir.parent.parent
config_path = root_dir / "config.py"

if config_path.exists():
    spec = importlib.util.spec_from_file_location("config", config_path)
    if spec and spec.loader:
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        config = config_module.config
    else:
        raise ImportError("Failed to load config spec")
else:
    raise ImportError("Config file not found")

# Import centralized prompts
prompts_path = root_dir / "prompts" / "batch_prompts.py"
if prompts_path.exists():
    spec = importlib.util.spec_from_file_location("batch_prompts", prompts_path)
    if spec and spec.loader:
        prompts_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prompts_module)
        BATCH_SYSTEM_PROMPT = prompts_module.BATCH_SYSTEM_PROMPT
        BATCH_USER_PROMPT = prompts_module.BATCH_USER_PROMPT
        BATCH_TEMPERATURE = prompts_module.BATCH_TEMPERATURE
        BATCH_MAX_TOKENS = prompts_module.BATCH_MAX_TOKENS
    else:
        # Fallback to embedded prompts if import fails
        BATCH_SYSTEM_PROMPT = """You are an expert document conversion assistant. Convert this document page to clean, professional Markdown format. Focus on accurate text extraction and proper structure while maintaining readability."""
        BATCH_USER_PROMPT = """Convert this document page to Markdown format with these specific requirements:

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
        BATCH_TEMPERATURE = 0.05
        BATCH_MAX_TOKENS = 8192
else:
    # Fallback to embedded prompts
    BATCH_SYSTEM_PROMPT = """You are an expert document conversion assistant. Convert this document page to clean, professional Markdown format. Focus on accurate text extraction and proper structure while maintaining readability."""
    BATCH_USER_PROMPT = """Convert this document page to Markdown format with these specific requirements:

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
    BATCH_TEMPERATURE = 0.05
    BATCH_MAX_TOKENS = 8192


class BatchPDFConverter:
    def __init__(self):
        self.client = OpenAI(
            api_key=config.OPENAI_API_KEY, base_url=config.OPENAI_API_BASE
        )
        self.model = config.OPENAI_DEFAULT_MODEL

    def _handle_openai_error(self, error, operation="API operation"):
        """Handle OpenAI API errors gracefully with user-friendly messages"""
        if isinstance(error, openai.BadRequestError):
            if "billing_hard_limit_reached" in str(error):
                print(f"💳 BILLING LIMIT REACHED")
                print(f"   Your OpenAI account has reached its billing hard limit.")
                print(f"   Please check your billing settings at: https://platform.openai.com/account/billing")
                print(f"   Current limit may need to be increased to continue processing.")
                return "billing_limit"
            elif "insufficient_quota" in str(error):
                print(f"💸 INSUFFICIENT QUOTA")
                print(f"   Your OpenAI account doesn't have enough credits for this operation.")
                print(f"   Please add credits at: https://platform.openai.com/account/billing")
                return "insufficient_quota"
            elif "rate_limit_exceeded" in str(error):
                print(f"⏳ RATE LIMIT EXCEEDED")
                print(f"   You've hit OpenAI's rate limits. This usually resolves automatically.")
                print(f"   The system will retry after a brief pause...")
                return "rate_limit"
            else:
                print(f"❌ BAD REQUEST: {error}")
                print(f"   The request was malformed or contained invalid parameters.")
                return "bad_request"
        
        elif isinstance(error, openai.AuthenticationError):
            print(f"🔐 AUTHENTICATION ERROR")
            print(f"   Your OpenAI API key is invalid or has been revoked.")
            print(f"   Please check your API key in the .env file.")
            print(f"   Get a new key at: https://platform.openai.com/account/api-keys")
            return "auth_error"
        
        elif isinstance(error, openai.PermissionDeniedError):
            print(f"🚫 PERMISSION DENIED")
            print(f"   Your API key doesn't have permission for this operation.")
            print(f"   Check your OpenAI plan and permissions.")
            return "permission_denied"
        
        elif isinstance(error, openai.NotFoundError):
            print(f"🔍 RESOURCE NOT FOUND")
            print(f"   The requested resource (batch, file, etc.) was not found.")
            print(f"   It may have been deleted or the ID is incorrect.")
            return "not_found"
        
        elif isinstance(error, openai.UnprocessableEntityError):
            print(f"⚠️  UNPROCESSABLE REQUEST")
            print(f"   The request was well-formed but couldn't be processed.")
            print(f"   This often happens with content policy violations or invalid input.")
            return "unprocessable"
        
        elif isinstance(error, openai.RateLimitError):
            print(f"🕐 RATE LIMIT ERROR")
            print(f"   You're making requests too quickly. Slowing down...")
            return "rate_limit"
        
        elif isinstance(error, openai.InternalServerError):
            print(f"🔧 OPENAI SERVER ERROR")
            print(f"   OpenAI's servers are experiencing issues.")
            print(f"   This is usually temporary - try again in a few minutes.")
            return "server_error"
        
        else:
            print(f"❌ UNEXPECTED ERROR during {operation}: {error}")
            print(f"   Error type: {type(error).__name__}")
            return "unknown_error"

    def _retry_with_exponential_backoff(self, func, max_retries=3, base_delay=1):
        """Retry function with exponential backoff for transient errors"""
        for attempt in range(max_retries):
            try:
                return func()
            except (openai.RateLimitError, openai.InternalServerError) as e:
                error_type = self._handle_openai_error(e, f"attempt {attempt + 1}")
                if attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)
                    print(f"   ⏳ Retrying in {delay} seconds... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(delay)
                else:
                    print(f"   ❌ All retry attempts failed")
                    raise
            except Exception as e:
                # Non-retryable errors
                self._handle_openai_error(e)
                raise

    def encode_image(self, image_path):
        """Convert image to base64 for API"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def extract_pdf_pages(self, pdf_path):
        """Extract pages from PDF as images"""
        # Import the core modules from src/core directory
        import sys
        from pathlib import Path

        # Add the src directory to path to access core modules
        src_dir = Path(__file__).parent.parent  # Go up to src/
        if str(src_dir) not in sys.path:
            sys.path.insert(0, str(src_dir))
        
        from core.PDFWorker import PDFWorker

        # Create temporary directory for this PDF
        pdf_name = Path(pdf_path).stem
        temp_dir = config.DEFAULT_TEMP_FOLDER / f"temp_batch/{pdf_name}"
        temp_dir.mkdir(parents=True, exist_ok=True)

        # Extract PDF pages
        worker = PDFWorker(pdf_path, 1, 0)  # All pages

        # Convert PDF to images in temp directory
        page_images = worker.convert_to_images(
            output_dir=str(temp_dir), dpi=200, fmt="jpg"
        )  # Lower DPI for faster processing

        # Create page mapping
        page_list = []
        for i, image_path in enumerate(page_images, 1):
            page_list.append((i, image_path))

        return page_list, temp_dir

    def create_batch_requests(self, pdf_files):
        """Create batch requests for all PDF pages"""
        batch_requests = []
        file_mapping = {}  # Maps custom_id to (pdf_name, page_num)

        for pdf_file in pdf_files:
            pdf_path = Path(str(config.DEFAULT_PDF_FOLDER)) / pdf_file
            if not pdf_path.exists():
                print(f"❌ PDF not found: {pdf_file}")
                continue

            print(f"📄 Extracting pages from {pdf_file}...")
            try:
                page_images, temp_dir = self.extract_pdf_pages(str(pdf_path))

                for page_num, image_path in page_images:
                    custom_id = f"{Path(pdf_file).stem}_page_{page_num:04d}"
                    file_mapping[custom_id] = (
                        Path(pdf_file).stem,
                        page_num,
                        str(temp_dir),
                    )  # Convert to string

                    # Encode image
                    base64_image = self.encode_image(image_path)

                    # Create batch request using centralized prompts
                    request = {
                        "custom_id": custom_id,
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": {
                            "model": self.model,
                            "messages": [
                                {"role": "system", "content": BATCH_SYSTEM_PROMPT},
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": BATCH_USER_PROMPT},
                                        {
                                            "type": "image_url",
                                            "image_url": {
                                                "url": f"data:image/jpeg;base64,{base64_image}"
                                            },
                                        },
                                    ],
                                },
                            ],
                            "temperature": BATCH_TEMPERATURE,
                            "max_tokens": BATCH_MAX_TOKENS,
                        },
                    }
                    batch_requests.append(request)

            except (OSError, ValueError) as e:
                print(f"❌ Error processing {pdf_file}: {e}")
                continue

        return batch_requests, file_mapping

    def submit_batch(self, requests, file_mapping):
        """Submit single batch to OpenAI Batch API for 50% cost savings"""
        # Always submit as single batch to get OpenAI Batch API 50% discount
        return self._submit_single_batch(requests, file_mapping)
    
    def _submit_single_batch(self, requests, file_mapping):
        """Submit a single batch with comprehensive error handling"""
        # Create temp directory for batch files
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        temp_batch_dir.mkdir(parents=True, exist_ok=True)
        
        # Create JSONL file in temp directory instead of root
        batch_file = temp_batch_dir / f"batch_requests_{int(time.time())}.jsonl"

        try:
            with open(batch_file, "w") as f:
                for request in requests:
                    f.write(json.dumps(request) + "\n")

            print(f"📤 Uploading batch file with {len(requests)} requests...")

            # Upload file with error handling
            def upload_file():
                with open(batch_file, "rb") as f:
                    return self.client.files.create(file=f, purpose="batch")
            
            try:
                batch_input_file = self._retry_with_exponential_backoff(upload_file)
            except Exception as e:
                error_type = self._handle_openai_error(e, "file upload")
                if error_type in ["billing_limit", "insufficient_quota", "auth_error"]:
                    print(f"\n🛑 CANNOT CONTINUE: Please resolve the above issue before retrying.")
                    # Clean up batch file on critical error
                    if batch_file.exists():
                        batch_file.unlink()
                    return None
                # Clean up batch file on any upload error
                if batch_file.exists():
                    batch_file.unlink()
                raise

            # Submit batch with error handling
            def submit_batch():
                return self.client.batches.create(
                    input_file_id=batch_input_file.id,
                    endpoint="/v1/chat/completions",
                    completion_window="24h",
                    metadata={"description": f"PDF conversion batch - {len(requests)} pages"},
                )
            
            try:
                batch = self._retry_with_exponential_backoff(submit_batch)
            except Exception as e:
                error_type = self._handle_openai_error(e, "batch submission")
                if error_type in ["billing_limit", "insufficient_quota", "auth_error"]:
                    print(f"\n🛑 CANNOT CONTINUE: Please resolve the above issue before retrying.")
                    # Clean up batch file on critical error
                    if batch_file.exists():
                        batch_file.unlink()
                    return None
                # Clean up batch file on any submission error
                if batch_file.exists():
                    batch_file.unlink()
                raise

            print("✅ Batch submitted successfully!")
            print(f"📋 Batch ID: {batch.id}")
            print(f"📊 Status: {batch.status}")
            print(f"🔢 Requests: {batch.request_counts}")

            # Save batch info for later retrieval
            batch_info = {
                "batch_id": batch.id,
                "file_mapping": file_mapping,
                "batch_file": str(batch_file),  # Store full path for potential cleanup
                "submitted_at": time.time(),
                "is_chunked": False
            }

            batch_info_file = temp_batch_dir / f"batch_info_{batch.id}.json"

            with open(batch_info_file, "w") as f:
                json.dump(batch_info, f, indent=2)

            # Clean up local batch file after successful submission
            if batch_file.exists():
                batch_file.unlink()

            return batch.id

        except Exception as e:
            # Force cleanup batch file on any error
            if batch_file.exists():
                try:
                    batch_file.unlink()
                    print(f"🧹 Cleaned up batch file: {batch_file.name}")
                except OSError:
                    print(f"⚠️  Could not remove batch file: {batch_file}")
            
            print(f"\n❌ BATCH SUBMISSION FAILED")
            print(f"   Error: {e}")
            print(f"   Please check your OpenAI account status and try again.")
            return None
        temp_batch_dir.mkdir(parents=True, exist_ok=True)
        batch_info_file = temp_batch_dir / f"batch_info_{batch.id}.json"

        with open(batch_info_file, "w") as f:
            json.dump(batch_info, f, indent=2)

        # Clean up local batch file
        os.remove(batch_file)

        return batch.id
    
    def _submit_chunked_batches(self, requests, file_mapping, chunk_size):
        """Submit multiple smaller batches sequentially to avoid token queue limits"""
        total_requests = len(requests)
        num_chunks = (total_requests + chunk_size - 1) // chunk_size  # Ceiling division
        
        print(f"🔄 Large batch detected! Splitting {total_requests} requests into {num_chunks} chunks of ~{chunk_size} each...")
        print(f"⚠️  Sequential submission mode enabled to avoid token queue limits")
        
        batch_ids = []
        chunk_mappings = []
        
        # Submit chunks one at a time with monitoring
        for chunk_idx in range(num_chunks):
            start_idx = chunk_idx * chunk_size
            end_idx = min(start_idx + chunk_size, total_requests)
            chunk_requests = requests[start_idx:end_idx]
            
            # Create file mapping for this chunk
            chunk_file_mapping = {}
            for request in chunk_requests:
                custom_id = request["custom_id"]
                if custom_id in file_mapping:
                    chunk_file_mapping[custom_id] = file_mapping[custom_id]
            
            print(f"📤 Submitting chunk {chunk_idx + 1}/{num_chunks} ({len(chunk_requests)} requests)...")
            
            # Submit this chunk
            try:
                chunk_batch_id = self._submit_single_batch(chunk_requests, chunk_file_mapping)
                batch_ids.append(chunk_batch_id)
                chunk_mappings.append(chunk_file_mapping)
                
                # If not the last chunk, wait for this chunk to start processing
                # to avoid overwhelming the token queue
                if chunk_idx < num_chunks - 1:
                    print(f"⏳ Waiting for chunk {chunk_idx + 1} to start processing...")
                    self._wait_for_chunk_start(chunk_batch_id)
                    
            except Exception as e:
                print(f"❌ Failed to submit chunk {chunk_idx + 1}: {e}")
                # Continue with remaining chunks
                continue
        
        if not batch_ids:
            raise RuntimeError("Failed to submit any batch chunks!")
        
        # Create master batch info for tracking all chunks
        master_batch_id = f"chunked_{int(time.time())}"
        master_batch_info = {
            "master_batch_id": master_batch_id,
            "chunk_batch_ids": batch_ids,
            "total_requests": total_requests,
            "num_chunks": len(batch_ids),
            "submitted_at": time.time(),
            "is_chunked": True,
            "file_mapping": file_mapping  # Keep full mapping for result reconstruction
        }
        
        # Save master batch info
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        temp_batch_dir.mkdir(parents=True, exist_ok=True)
        master_batch_file = temp_batch_dir / f"batch_info_{master_batch_id}.json"
        
        with open(master_batch_file, "w") as f:
            json.dump(master_batch_info, f, indent=2)
        
        print(f"✅ All chunks submitted successfully!")
        print(f"📋 Master Batch ID: {master_batch_id}")
        print(f"🔢 Total Chunks: {len(batch_ids)}")
        print(f"📊 Individual Batch IDs: {batch_ids}")
        
        return master_batch_id
    
    def _wait_for_chunk_start(self, batch_id, max_wait_time=120):
        """Wait for a batch to start processing (move from 'validating' to 'in_progress')"""
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            try:
                batch = self.client.batches.retrieve(batch_id)
                status = batch.status
                
                if status in ["in_progress", "completed", "failed"]:
                    print(f"   ✅ Chunk {batch_id[-8:]} is now {status}")
                    return True
                elif status == "validating":
                    print(f"   ⏳ Chunk {batch_id[-8:]} still validating...")
                    time.sleep(10)
                else:
                    print(f"   ⚠️  Unexpected status: {status}")
                    time.sleep(5)
                    
            except Exception as e:
                print(f"   ❌ Error checking chunk status: {e}")
                time.sleep(10)
        
        print(f"   ⚠️  Timeout waiting for chunk to start, continuing anyway...")
        return False

    def check_batch_status(self, batch_id):
        """Check batch processing status (handles both single and chunked batches)"""
        # Check if this is a chunked batch
        if batch_id.startswith("chunked_"):
            return self._check_chunked_batch_status(batch_id)
        else:
            return self._check_single_batch_status(batch_id)
    
    def _check_single_batch_status(self, batch_id):
        """Check status of a single batch with error handling"""
        def get_batch_status():
            return self.client.batches.retrieve(batch_id)
        
        try:
            batch = self._retry_with_exponential_backoff(get_batch_status)
            print(f"📋 Batch ID: {batch_id}")
            print(f"📊 Status: {batch.status}")
            print(f"🔢 Request counts: {batch.request_counts}")
            print(f"⏱️  Created: {batch.created_at}")

            if batch.completed_at:
                print(f"✅ Completed: {batch.completed_at}")

            if batch.failed_at:
                print(f"❌ Failed: {batch.failed_at}")

            return batch
        except Exception as e:
            error_type = self._handle_openai_error(e, "batch status check")
            if error_type == "not_found":
                print(f"   This may indicate the batch was cancelled or expired.")
            elif error_type in ["billing_limit", "auth_error"]:
                print(f"   Cannot check batch status due to account issues.")
            return None
    
    def _check_chunked_batch_status(self, master_batch_id):
        """Check status of all chunks in a chunked batch"""
        # Load master batch info
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        master_batch_file = temp_batch_dir / f"batch_info_{master_batch_id}.json"
        
        if not master_batch_file.exists():
            print(f"❌ Master batch info not found: {master_batch_id}")
            return None
        
        try:
            with open(master_batch_file) as f:
                master_info = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"❌ Error loading master batch info: {e}")
            return None
        
        chunk_batch_ids = master_info.get("chunk_batch_ids", [])
        master_total_requests = master_info.get("total_requests", 0)  # Get total from master info
        
        if not chunk_batch_ids:
            print(f"❌ No chunk batch IDs found in master batch")
            return None
        
        print(f"📋 Master Batch ID: {master_batch_id}")
        print(f"🔢 Total Chunks: {len(chunk_batch_ids)}")
        print(f"📊 Total Requests: {master_total_requests}")
        print(f"📊 Checking status of all chunks...")
        
        completed_chunks = 0
        failed_chunks = 0
        in_progress_chunks = 0
        total_completed_requests = 0
        
        chunk_statuses = []
        
        for i, chunk_id in enumerate(chunk_batch_ids, 1):
            try:
                batch = self.client.batches.retrieve(chunk_id)
                status = batch.status
                request_counts = batch.request_counts
                
                if request_counts and hasattr(request_counts, 'completed'):
                    completed = getattr(request_counts, 'completed', 0) or 0
                    # For failed batches with 0/0, we can't get the original total from API
                    # We'll estimate based on chunk position and master total
                    if status == "failed" and completed == 0:
                        # Don't add failed requests to total_completed_requests
                        pass
                    else:
                        total_completed_requests += completed
                else:
                    completed = 0
                
                print(f"   📦 Chunk {i}/{len(chunk_batch_ids)}: {status} ({completed} completed)")
                
                if status == "completed":
                    completed_chunks += 1
                elif status == "failed":
                    failed_chunks += 1
                else:
                    in_progress_chunks += 1
                
                chunk_statuses.append({
                    "chunk_id": chunk_id,
                    "status": status,
                    "completed": completed,
                    "total": 0  # We'll use master_total_requests for overall progress
                })
                
            except Exception as e:
                print(f"   ❌ Chunk {i}: Error checking status - {e}")
                failed_chunks += 1
                chunk_statuses.append({
                    "chunk_id": chunk_id,
                    "status": "error",
                    "completed": 0,
                    "total": 0
                })
        
        # Summary
        print(f"\n📊 Overall Status:")
        print(f"   ✅ Completed chunks: {completed_chunks}/{len(chunk_batch_ids)}")
        print(f"   🔄 In progress chunks: {in_progress_chunks}/{len(chunk_batch_ids)}")
        print(f"   ❌ Failed chunks: {failed_chunks}/{len(chunk_batch_ids)}")
        print(f"   📄 Total requests: {total_completed_requests}/{master_total_requests}")
        
        if master_total_requests > 0:
            progress_pct = (total_completed_requests / master_total_requests) * 100
            print(f"   📈 Overall progress: {progress_pct:.1f}%")
        
        # Return a summary object
        return {
            "master_batch_id": master_batch_id,
            "chunk_statuses": chunk_statuses,
            "completed_chunks": completed_chunks,
            "total_chunks": len(chunk_batch_ids),
            "completed_requests": total_completed_requests,
            "total_requests": master_total_requests,
            "all_completed": completed_chunks == len(chunk_batch_ids),
            "any_failed": failed_chunks > 0
        }

    def retrieve_results(self, batch_id):
        """Retrieve and process batch results (handles both single and chunked batches)"""
        # Check if this is a chunked batch
        if batch_id.startswith("chunked_"):
            return self._retrieve_chunked_results(batch_id)
        else:
            return self._retrieve_single_results(batch_id)
    
    def _retrieve_single_results(self, batch_id):
        """Retrieve results from a single batch (original logic)"""
        # Load batch info from temp directory
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        batch_info_file = temp_batch_dir / f"batch_info_{batch_id}.json"
        file_mapping = {}

        if batch_info_file.exists():
            try:
                with open(batch_info_file) as f:
                    batch_info = json.load(f)
                file_mapping = batch_info.get("file_mapping", {})
            except (json.JSONDecodeError, OSError) as e:
                print(
                    f"⚠️  Corrupted batch info file, will reconstruct from results: {e}"
                )
                file_mapping = {}

        # Get batch results
        try:
            batch = self.client.batches.retrieve(batch_id)

            if batch.status not in ["completed"]:
                print(f"❌ Batch not completed yet. Status: {batch.status}")
                if hasattr(batch, "request_counts") and batch.request_counts:
                    completed = getattr(batch.request_counts, "completed", 0)
                    total = getattr(batch.request_counts, "total", 1)
                    print(f"📊 Progress: {completed}/{total}")

                    # Allow partial retrieval if 90%+ complete
                    if completed >= total * 0.9:
                        print("⚠️  Attempting partial retrieval (90%+ complete)")
                    else:
                        return False
                else:
                    return False

            # Download results
            result_file_id = batch.output_file_id
            if not result_file_id:
                print(f"❌ No output file available for batch {batch_id}")
                return False

            result = self.client.files.content(result_file_id)

            # Parse results and reconstruct file mapping if needed
            results = {}
            usage_stats = {}  # Track usage per page
            for line in result.text.split("\n"):
                if line.strip():
                    try:
                        result_item = json.loads(line)
                        custom_id = result_item.get("custom_id")
                        if custom_id and result_item.get("response"):
                            content = result_item["response"]["body"]["choices"][0][
                                "message"
                            ]["content"]
                            results[custom_id] = content

                            # Extract usage statistics
                            if "usage" in result_item["response"]["body"]:
                                usage = result_item["response"]["body"]["usage"]
                                usage_stats[custom_id] = {
                                    "prompt_tokens": usage.get("prompt_tokens", 0),
                                    "completion_tokens": usage.get(
                                        "completion_tokens", 0
                                    ),
                                    "total_tokens": usage.get("total_tokens", 0),
                                    "input_cost": (
                                        usage.get("prompt_tokens", 0) / 1_000_000
                                    )
                                    * 0.150,
                                    "output_cost": (
                                        usage.get("completion_tokens", 0) / 1_000_000
                                    )
                                    * 0.600,
                                    "total_cost": (
                                        (usage.get("prompt_tokens", 0) / 1_000_000)
                                        * 0.150
                                    )
                                    + (
                                        (usage.get("completion_tokens", 0) / 1_000_000)
                                        * 0.600
                                    ),
                                }

                            # Reconstruct file mapping if missing
                            if custom_id not in file_mapping:
                                # Parse custom_id format: PDF-NAME_page_0001
                                parts = custom_id.split("_page_")
                                if len(parts) == 2:
                                    pdf_name = parts[0]
                                    page_num = int(parts[1])
                                    file_mapping[custom_id] = (
                                        pdf_name,
                                        page_num,
                                        f"temp_batch/{pdf_name}",
                                    )

                    except (
                        json.JSONDecodeError,
                        KeyError,
                        ValueError,
                        IndexError,
                    ) as e:
                        print(f"⚠️  Error parsing result line: {e}")

            # Group results by PDF and create final markdown files
            pdf_contents = {}
            pdf_usage_stats = {}  # Track usage per PDF

            for custom_id, content in results.items():
                if custom_id in file_mapping:
                    pdf_name, page_num, temp_dir = file_mapping[custom_id]

                    if pdf_name not in pdf_contents:
                        pdf_contents[pdf_name] = {}
                        pdf_usage_stats[pdf_name] = {
                            "total_tokens": 0,
                            "total_cost": 0.0,
                            "prompt_tokens": 0,
                            "completion_tokens": 0,
                            "page_count": 0,
                        }

                    pdf_contents[pdf_name][page_num] = content

                    # Accumulate usage stats for this PDF
                    if custom_id in usage_stats:
                        stats = usage_stats[custom_id]
                        pdf_usage_stats[pdf_name]["total_tokens"] += stats[
                            "total_tokens"
                        ]
                        pdf_usage_stats[pdf_name]["total_cost"] += stats["total_cost"]
                        pdf_usage_stats[pdf_name]["prompt_tokens"] += stats[
                            "prompt_tokens"
                        ]
                        pdf_usage_stats[pdf_name]["completion_tokens"] += stats[
                            "completion_tokens"
                        ]
                        pdf_usage_stats[pdf_name]["page_count"] += 1

            # Create final markdown files
            os.makedirs(str(config.DEFAULT_CONVERTED_FOLDER), exist_ok=True)

            for pdf_name, pages in pdf_contents.items():
                output_file = (
                    Path(str(config.DEFAULT_CONVERTED_FOLDER)) / f"{pdf_name}_batch.md"
                )
                usage_data = pdf_usage_stats.get(pdf_name, {})

                with open(output_file, "w", encoding="utf-8") as f:
                    for page_num in sorted(pages.keys()):
                        f.write(f"---\n# Page {page_num}\n---\n\n")
                        f.write(pages[page_num])
                        f.write("\n\n")

                    # Add comprehensive metadata including usage statistics
                    f.write("---\n\n## Processing Metadata\n\n")
                    f.write(f"- **Document:** {pdf_name}\n")
                    f.write(f"- **Total Pages:** {len(pages)}\n")
                    f.write("- **Processing Method:** OpenAI Batch API\n")
                    f.write(f"- **Model:** {self.model}\n")
                    f.write(f"- **Batch ID:** {batch_id}\n")
                    f.write(
                        f"- **Processed:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                    )

                    # Add usage and cost information
                    if usage_data and usage_data.get("page_count", 0) > 0:
                        f.write("### 📊 Processing Statistics\n\n")
                        f.write(
                            f"- **Total Tokens Used:** {usage_data['total_tokens']:,}\n"
                        )
                        f.write(
                            f"- **Prompt Tokens:** {usage_data['prompt_tokens']:,}\n"
                        )
                        f.write(
                            f"- **Completion Tokens:** {usage_data['completion_tokens']:,}\n"
                        )
                        f.write(
                            f"- **Total Processing Cost:** ${usage_data['total_cost']:.4f}\n"
                        )
                        f.write(
                            f"- **Average Tokens per Page:** {usage_data['total_tokens'] / usage_data['page_count']:.0f}\n"
                        )
                        f.write(
                            f"- **Average Cost per Page:** ${usage_data['total_cost'] / usage_data['page_count']:.4f}\n\n"
                        )

                        # Cost breakdown
                        input_cost = (usage_data["prompt_tokens"] / 1_000_000) * 0.150
                        output_cost = (
                            usage_data["completion_tokens"] / 1_000_000
                        ) * 0.600
                        f.write("### 💰 Cost Breakdown\n\n")
                        f.write(
                            f"- **Input Processing:** ${input_cost:.4f} (vision + text)\n"
                        )
                        f.write(
                            f"- **Output Generation:** ${output_cost:.4f} (markdown text)\n"
                        )
                        f.write("- **Batch API Discount:** 50% off regular pricing\n")
                        f.write(
                            f"- **Estimated Regular Cost:** ${usage_data['total_cost'] * 2:.4f}\n\n"
                        )

                        # Efficiency metrics
                        tokens_per_dollar = (
                            usage_data["total_tokens"] / usage_data["total_cost"]
                            if usage_data["total_cost"] > 0
                            else 0
                        )
                        pages_per_dollar = (
                            usage_data["page_count"] / usage_data["total_cost"]
                            if usage_data["total_cost"] > 0
                            else 0
                        )
                        f.write("### ⚡ Efficiency Metrics\n\n")
                        f.write(f"- **Tokens per Dollar:** {tokens_per_dollar:.0f}\n")
                        f.write(f"- **Pages per Dollar:** {pages_per_dollar:.1f}\n")
                        f.write("- **Processing Method:** Batch API (cost-optimized)\n")

                print(f"✅ Created: {output_file} ({len(pages)} pages)")

                # Print individual document stats
                if usage_data and usage_data.get("page_count", 0) > 0:
                    print(
                        f"   💰 Cost: ${usage_data['total_cost']:.4f} | 🔢 Tokens: {usage_data['total_tokens']:,} | 📄 Avg: ${usage_data['total_cost'] / usage_data['page_count']:.4f}/page"
                    )

            # Cleanup temp directories (skip if reconstructed mapping)
            if file_mapping:
                for custom_id in list(file_mapping.keys())[
                    :5
                ]:  # Only check a few to avoid errors
                    try:
                        _, _, temp_dir_str = file_mapping[custom_id]
                        temp_dir = Path(temp_dir_str)
                        if temp_dir.exists():
                            shutil.rmtree(temp_dir, ignore_errors=True)
                    except (OSError, PermissionError, RuntimeError):
                        continue  # Skip cleanup errors

            # Cleanup temp_batch directory if empty
            temp_batch_dir = Path("temp_batch")
            if temp_batch_dir.exists() and not any(temp_batch_dir.iterdir()):
                temp_batch_dir.rmdir()

            print(
                f"🎉 Batch processing completed! Generated {len(pdf_contents)} markdown files."
            )
            return True

        except (OSError, RuntimeError, ValueError) as e:
            print(f"❌ Error retrieving results: {e}")
            return False
    
    def _retrieve_chunked_results(self, master_batch_id):
        """Retrieve and combine results from all chunks in a chunked batch"""
        # Load master batch info
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        master_batch_file = temp_batch_dir / f"batch_info_{master_batch_id}.json"
        
        if not master_batch_file.exists():
            print(f"❌ Master batch info not found: {master_batch_id}")
            return False
        
        try:
            with open(master_batch_file) as f:
                master_info = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"❌ Error loading master batch info: {e}")
            return False
        
        chunk_batch_ids = master_info.get("chunk_batch_ids", [])
        file_mapping = master_info.get("file_mapping", {})
        
        if not chunk_batch_ids:
            print(f"❌ No chunk batch IDs found in master batch")
            return False
        
        print(f"📥 Retrieving results from {len(chunk_batch_ids)} batch chunks...")
        
        # Check if all chunks are completed
        incomplete_chunks = []
        for i, chunk_id in enumerate(chunk_batch_ids, 1):
            try:
                batch = self.client.batches.retrieve(chunk_id)
                if batch.status != "completed":
                    incomplete_chunks.append(f"Chunk {i} ({chunk_id}): {batch.status}")
            except Exception as e:
                incomplete_chunks.append(f"Chunk {i} ({chunk_id}): Error - {e}")
        
        if incomplete_chunks:
            print(f"❌ Some chunks are not completed yet:")
            for incomplete in incomplete_chunks:
                print(f"   {incomplete}")
            return False
        
        # Collect results from all chunks
        all_results = {}
        all_usage_stats = {}
        
        for i, chunk_id in enumerate(chunk_batch_ids, 1):
            print(f"📥 Retrieving chunk {i}/{len(chunk_batch_ids)}...")
            
            try:
                batch = self.client.batches.retrieve(chunk_id)
                result_file_id = batch.output_file_id
                
                if not result_file_id:
                    print(f"⚠️  No output file for chunk {i}, skipping...")
                    continue
                
                result = self.client.files.content(result_file_id)
                
                # Parse chunk results
                for line in result.text.split("\n"):
                    if line.strip():
                        try:
                            result_item = json.loads(line)
                            custom_id = result_item.get("custom_id")
                            if custom_id and result_item.get("response"):
                                content = result_item["response"]["body"]["choices"][0]["message"]["content"]
                                all_results[custom_id] = content
                                
                                # Extract usage statistics
                                if "usage" in result_item["response"]["body"]:
                                    usage = result_item["response"]["body"]["usage"]
                                    all_usage_stats[custom_id] = {
                                        "prompt_tokens": usage.get("prompt_tokens", 0),
                                        "completion_tokens": usage.get("completion_tokens", 0),
                                        "total_tokens": usage.get("total_tokens", 0),
                                        "input_cost": (usage.get("prompt_tokens", 0) / 1_000_000) * 0.150,
                                        "output_cost": (usage.get("completion_tokens", 0) / 1_000_000) * 0.600,
                                        "total_cost": ((usage.get("prompt_tokens", 0) / 1_000_000) * 0.150) + 
                                                    ((usage.get("completion_tokens", 0) / 1_000_000) * 0.600),
                                    }
                        except (json.JSONDecodeError, KeyError, ValueError, IndexError) as e:
                            print(f"⚠️  Error parsing result line in chunk {i}: {e}")
                            
            except Exception as e:
                print(f"❌ Error retrieving chunk {i}: {e}")
                continue
        
        print(f"✅ Retrieved {len(all_results)} results from all chunks")
        
        # Group results by PDF and create final markdown files (same logic as single batch)
        pdf_contents = {}
        pdf_usage_stats = {}
        
        for custom_id, content in all_results.items():
            if custom_id in file_mapping:
                pdf_name, page_num, temp_dir = file_mapping[custom_id]
                
                if pdf_name not in pdf_contents:
                    pdf_contents[pdf_name] = {}
                    pdf_usage_stats[pdf_name] = {
                        "total_tokens": 0,
                        "total_cost": 0.0,
                        "prompt_tokens": 0,
                        "completion_tokens": 0,
                        "page_count": 0,
                    }
                
                pdf_contents[pdf_name][page_num] = content
                
                # Accumulate usage stats for this PDF
                if custom_id in all_usage_stats:
                    stats = all_usage_stats[custom_id]
                    pdf_usage_stats[pdf_name]["total_tokens"] += stats["total_tokens"]
                    pdf_usage_stats[pdf_name]["total_cost"] += stats["total_cost"]
                    pdf_usage_stats[pdf_name]["prompt_tokens"] += stats["prompt_tokens"]
                    pdf_usage_stats[pdf_name]["completion_tokens"] += stats["completion_tokens"]
                    pdf_usage_stats[pdf_name]["page_count"] += 1
        
        # Create final markdown files (same as single batch)
        os.makedirs(str(config.DEFAULT_CONVERTED_FOLDER), exist_ok=True)
        
        for pdf_name, pages in pdf_contents.items():
            output_file = Path(str(config.DEFAULT_CONVERTED_FOLDER)) / f"{pdf_name}_batch.md"
            usage_data = pdf_usage_stats.get(pdf_name, {})
            
            with open(output_file, "w", encoding="utf-8") as f:
                for page_num in sorted(pages.keys()):
                    f.write(f"---\n# Page {page_num}\n---\n\n")
                    f.write(pages[page_num])
                    f.write("\n\n")
                
                # Add comprehensive metadata including usage statistics
                f.write("---\n\n## Processing Metadata\n\n")
                f.write(f"- **Document:** {pdf_name}\n")
                f.write(f"- **Total Pages:** {len(pages)}\n")
                f.write("- **Processing Method:** OpenAI Batch API (Chunked)\n")
                f.write(f"- **Model:** {self.model}\n")
                f.write(f"- **Master Batch ID:** {master_batch_id}\n")
                f.write(f"- **Chunks:** {len(chunk_batch_ids)}\n")
                f.write(f"- **Processed:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Add usage and cost information (same as single batch)
                if usage_data and usage_data.get("page_count", 0) > 0:
                    f.write("### 📊 Processing Statistics\n\n")
                    f.write(f"- **Total Tokens Used:** {usage_data['total_tokens']:,}\n")
                    f.write(f"- **Prompt Tokens:** {usage_data['prompt_tokens']:,}\n")
                    f.write(f"- **Completion Tokens:** {usage_data['completion_tokens']:,}\n")
                    f.write(f"- **Total Processing Cost:** ${usage_data['total_cost']:.4f}\n")
                    f.write(f"- **Average Tokens per Page:** {usage_data['total_tokens'] / usage_data['page_count']:.0f}\n")
                    f.write(f"- **Average Cost per Page:** ${usage_data['total_cost'] / usage_data['page_count']:.4f}\n\n")
                    
                    # Cost breakdown
                    input_cost = (usage_data["prompt_tokens"] / 1_000_000) * 0.150
                    output_cost = (usage_data["completion_tokens"] / 1_000_000) * 0.600
                    f.write("### 💰 Cost Breakdown\n\n")
                    f.write(f"- **Input Processing:** ${input_cost:.4f} (vision + text)\n")
                    f.write(f"- **Output Generation:** ${output_cost:.4f} (markdown text)\n")
                    f.write("- **Batch API Discount:** 50% off regular pricing\n")
                    f.write(f"- **Estimated Regular Cost:** ${usage_data['total_cost'] * 2:.4f}\n\n")
                    
                    # Efficiency metrics
                    tokens_per_dollar = (usage_data["total_tokens"] / usage_data["total_cost"] 
                                       if usage_data["total_cost"] > 0 else 0)
                    pages_per_dollar = (usage_data["page_count"] / usage_data["total_cost"] 
                                      if usage_data["total_cost"] > 0 else 0)
                    f.write("### ⚡ Efficiency Metrics\n\n")
                    f.write(f"- **Tokens per Dollar:** {tokens_per_dollar:.0f}\n")
                    f.write(f"- **Pages per Dollar:** {pages_per_dollar:.1f}\n")
                    f.write("- **Processing Method:** Chunked Batch API (cost-optimized)\n")
            
            print(f"✅ Created: {output_file} ({len(pages)} pages)")
            
            # Print individual document stats
            if usage_data and usage_data.get("page_count", 0) > 0:
                print(f"   💰 Cost: ${usage_data['total_cost']:.4f} | 🔢 Tokens: {usage_data['total_tokens']:,} | 📄 Avg: ${usage_data['total_cost'] / usage_data['page_count']:.4f}/page")
        
        print(f"🎉 Chunked batch processing completed! Generated {len(pdf_contents)} markdown files.")
        return True


def main():
    converter = BatchPDFConverter()

    if len(sys.argv) < 2:
        print("Usage:")
        print(
            "  python batch_api.py submit         # Submit all PDFs for batch processing"
        )
        print("  python batch_api.py status <id>    # Check batch status")
        print("  python batch_api.py retrieve <id>  # Retrieve batch results")
        print("  python batch_api.py list           # List pending batches")
        print("  python batch_api.py cleanup        # Clean up orphaned batch files")
        return

    command = sys.argv[1].lower()

    if command == "submit":
        # Get all PDF files
        pdf_dir = Path(str(config.DEFAULT_PDF_FOLDER))
        if not pdf_dir.exists():
            print("❌ PDFs directory not found!")
            return

        pdf_files = [f.name for f in pdf_dir.glob("*.pdf")]
        if not pdf_files:
            print("❌ No PDF files found!")
            return

        print(f"🚀 Starting batch processing for {len(pdf_files)} PDFs...")
        print("📋 Files to process:", pdf_files)

        # Create batch requests
        requests, file_mapping = converter.create_batch_requests(pdf_files)

        if not requests:
            print("❌ No valid requests created!")
            return

        # Submit batch
        batch_id = converter.submit_batch(requests, file_mapping)
        if batch_id:
            print("\n✅ Batch submitted! Use this ID to check status:")
            print(f"   python batch_api.py status {batch_id}")
            print(f"   python batch_api.py retrieve {batch_id}")
        else:
            print("\n❌ Batch submission failed. Check error messages above.")

    elif command == "status":
        if len(sys.argv) < 3:
            print("❌ Please provide batch ID")
            return
        batch_id = sys.argv[2]
        converter.check_batch_status(batch_id)

    elif command == "retrieve":
        if len(sys.argv) < 3:
            print("❌ Please provide batch ID")
            return
        batch_id = sys.argv[2]
        converter.retrieve_results(batch_id)

    elif command == "cleanup":
        # Use centralized cleanup manager
        try:
            # Import the centralized cleanup manager
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from utils.cleanup_manager import CleanupManager
            
            cleanup_manager = CleanupManager(verbose=True)
            cleanup_manager.cleanup_batch_files()
        except ImportError as e:
            print(f"⚠️  Could not import centralized cleanup manager: {e}")
            print("   Falling back to basic cleanup...")
            
            # Minimal fallback cleanup
            cleaned = 0
            root_dir = Path.cwd()
            
            # Clean essential batch files
            for pattern in ["batch_requests_*.jsonl", "batch_info_*.json", "usage_stats_*.json"]:
                for item in root_dir.glob(pattern):
                    try:
                        item.unlink()
                        print(f"   🗑️  Removed: {item.name}")
                        cleaned += 1
                    except OSError as e:
                        print(f"   ⚠️  Could not remove {item.name}: {e}")
            
            print(f"✅ Basic cleanup completed! Removed {cleaned} files.")

    elif command == "list":
        # List all batch info files from temp directory
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        if temp_batch_dir.exists():
            batch_files = temp_batch_dir.glob("batch_info_*.json")
            for batch_file in batch_files:
                batch_id = batch_file.name.replace("batch_info_", "").replace(
                    ".json", ""
                )
                print(f"📋 Found batch: {batch_id}")
                converter.check_batch_status(batch_id)
                print()
        else:
            print("📋 No batch files found")


if __name__ == "__main__":
    main()
