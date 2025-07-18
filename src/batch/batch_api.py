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
import sys
import time
from pathlib import Path

from openai import OpenAI

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


class BatchPDFConverter:
    def __init__(self):
        self.client = OpenAI(
            api_key=config.OPENAI_API_KEY, base_url=config.OPENAI_API_BASE
        )
        self.model = config.OPENAI_DEFAULT_MODEL

    def encode_image(self, image_path):
        """Convert image to base64 for API"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def extract_pdf_pages(self, pdf_path):
        """Extract pages from PDF as images"""
        # Import the core modules from converted directory
        import sys

        sys.path.append(str(config.DEFAULT_CONVERTED_FOLDER))
        from core.PDFWorker import PDFWorker

        # Create temporary directory for this PDF
        pdf_name = Path(pdf_path).stem
        temp_dir = config.DEFAULT_TEMP_FOLDER / f"temp_batch/{pdf_name}"
        temp_dir.mkdir(parents=True, exist_ok=True)

        # Extract PDF pages
        worker = PDFWorker(pdf_path, 1, 0)  # All pages

        # Convert PDF to images
        original_output_dir = worker.output_dir
        worker.output_dir = str(temp_dir)  # Set temp directory as output

        page_images = worker.convert_to_images(
            dpi=200, fmt="jpg"
        )  # Lower DPI for faster processing

        # Restore original output directory
        worker.output_dir = original_output_dir

        # Create page mapping
        page_list = []
        for i, image_path in enumerate(page_images, 1):
            page_list.append((i, image_path))

        return page_list, temp_dir

    def create_batch_requests(self, pdf_files):
        """Create batch requests for all PDF pages"""
        batch_requests = []
        file_mapping = {}  # Maps custom_id to (pdf_name, page_num)

        system_prompt = """You are an expert document conversion assistant. Convert this document page to clean, professional Markdown format. Focus on accurate text extraction and proper structure while maintaining readability."""

        user_prompt = """Convert this document page to Markdown format with these specific requirements:

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

                    # Create batch request
                    request = {
                        "custom_id": custom_id,
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": {
                            "model": self.model,
                            "messages": [
                                {"role": "system", "content": system_prompt},
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": user_prompt},
                                        {
                                            "type": "image_url",
                                            "image_url": {
                                                "url": f"data:image/jpeg;base64,{base64_image}"
                                            },
                                        },
                                    ],
                                },
                            ],
                            "temperature": 0.05,  # Very low for consistency
                            "max_tokens": 8192,  # Higher for complete conversion
                        },
                    }
                    batch_requests.append(request)

            except (OSError, ValueError) as e:
                print(f"❌ Error processing {pdf_file}: {e}")
                continue

        return batch_requests, file_mapping

    def submit_batch(self, requests, file_mapping):
        """Submit batch to OpenAI"""
        # Create JSONL file
        batch_file = f"batch_requests_{int(time.time())}.jsonl"

        with open(batch_file, "w") as f:
            for request in requests:
                f.write(json.dumps(request) + "\n")

        print(f"📤 Uploading batch file with {len(requests)} requests...")

        # Upload file
        with open(batch_file, "rb") as f:
            batch_input_file = self.client.files.create(file=f, purpose="batch")

        # Submit batch
        batch = self.client.batches.create(
            input_file_id=batch_input_file.id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={"description": f"PDF conversion batch - {len(requests)} pages"},
        )

        print("✅ Batch submitted successfully!")
        print(f"📋 Batch ID: {batch.id}")
        print(f"📊 Status: {batch.status}")
        print(f"🔢 Requests: {batch.request_counts}")

        # Save batch info for later retrieval
        batch_info = {
            "batch_id": batch.id,
            "file_mapping": file_mapping,
            "batch_file": batch_file,
            "submitted_at": time.time(),
        }

        # Save batch info to temp directory instead of root
        temp_batch_dir = config.DEFAULT_TEMP_FOLDER / "temp_batch"
        temp_batch_dir.mkdir(parents=True, exist_ok=True)
        batch_info_file = temp_batch_dir / f"batch_info_{batch.id}.json"

        with open(batch_info_file, "w") as f:
            json.dump(batch_info, f, indent=2)

        # Clean up local batch file
        os.remove(batch_file)

        return batch.id

    def check_batch_status(self, batch_id):
        """Check batch processing status"""
        try:
            batch = self.client.batches.retrieve(batch_id)
            print(f"📋 Batch ID: {batch_id}")
            print(f"📊 Status: {batch.status}")
            print(f"🔢 Request counts: {batch.request_counts}")
            print(f"⏱️  Created: {batch.created_at}")

            if batch.completed_at:
                print(f"✅ Completed: {batch.completed_at}")

            if batch.failed_at:
                print(f"❌ Failed: {batch.failed_at}")

            return batch
        except (RuntimeError, ValueError, KeyError) as e:
            print(f"❌ Error checking batch: {e}")
            return None

    def retrieve_results(self, batch_id):
        """Retrieve and process batch results"""
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
                            import shutil

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
        print("\n✅ Batch submitted! Use this ID to check status:")
        print(f"   python batch_api.py status {batch_id}")
        print(f"   python batch_api.py retrieve {batch_id}")

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
