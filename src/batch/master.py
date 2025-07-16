#!/usr/bin/env python3
"""
PDF Batch Master - Complete batch processing management
Handles submission, monitoring, retrieval, and consolidation
"""

import os
import json
import time
import subprocess
import sys
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import shutil

# Load environment variables
load_dotenv()

class PDFBatchMaster:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
        )
        self.model = os.getenv("OPENAI_DEFAULT_MODEL", "gpt-4o-mini")

    def print_status(self, message, level="INFO"):
        """Print formatted status messages"""
        timestamp = time.strftime('%H:%M:%S')
        symbols = {
            "INFO": "ℹ️",
            "SUCCESS": "✅",
            "WARNING": "⚠️",
            "ERROR": "❌",
            "PROGRESS": "🔄"
        }
        symbol = symbols.get(level, "📋")
        print(f"{symbol} [{timestamp}] {message}")

    def submit_new_batch(self):
        """Submit a new batch for processing"""
        self.print_status("Starting new batch submission", "PROGRESS")

        try:
            result = subprocess.run([
                sys.executable, "batch_api.py", "submit"
            ], capture_output=True, text=True, encoding='utf-8', errors='replace')

            if result.returncode == 0:
                # Extract batch ID from output
                lines = result.stdout.split('\n')
                batch_id = None
                for line in lines:
                    if "Batch ID:" in line:
                        batch_id = line.split("Batch ID:")[-1].strip()
                        break

                if batch_id:
                    self.print_status(f"Batch submitted successfully: {batch_id}", "SUCCESS")
                    return batch_id
                else:
                    self.print_status("Could not extract batch ID from output", "WARNING")
                    print(result.stdout)
                    return None
            else:
                self.print_status("Failed to submit batch", "ERROR")
                print(result.stderr)
                return None

        except Exception as e:
            self.print_status(f"Error submitting batch: {e}", "ERROR")
            return None

    def check_batch_status(self, batch_id):
        """Check batch status and return parsed info"""
        try:
            batch = self.client.batches.retrieve(batch_id)

            # Extract usage statistics if available
            usage_info = {}
            if hasattr(batch, 'request_counts') and batch.request_counts:
                if hasattr(batch.request_counts, 'completed') and batch.request_counts.completed > 0:
                    # Try to get usage data from metadata or other fields
                    if hasattr(batch, 'metadata') and batch.metadata:
                        usage_info = batch.metadata

            return {
                'id': batch_id,
                'status': batch.status,
                'completed': batch.request_counts.completed if batch.request_counts else 0,
                'failed': batch.request_counts.failed if batch.request_counts else 0,
                'total': batch.request_counts.total if batch.request_counts else 0,
                'created_at': batch.created_at,
                'completed_at': batch.completed_at,
                'failed_at': batch.failed_at,
                'usage': usage_info
            }
        except Exception as e:
            self.print_status(f"Error checking batch {batch_id}: {e}", "ERROR")
            return None

    def analyze_batch_usage(self, batch_id):
        """Analyze batch usage and costs from completed results"""
        self.print_status(f"Analyzing usage for batch {batch_id}", "PROGRESS")

        try:
            # Get the batch info
            batch = self.client.batches.retrieve(batch_id)

            if batch.status != "completed":
                self.print_status("Batch not completed, usage analysis unavailable", "WARNING")
                return None

            # Try to get the output file
            if not batch.output_file_id:
                self.print_status("No output file available for usage analysis", "WARNING")
                return None

            # Download and analyze the output file
            output_response = self.client.files.content(batch.output_file_id)
            output_content = output_response.content.decode('utf-8')

            total_tokens = 0
            total_cost = 0.0
            request_count = 0
            token_breakdown = {
                'prompt_tokens': 0,
                'completion_tokens': 0,
                'total_tokens': 0
            }

            # Parse each line (JSONL format)
            for line in output_content.strip().split('\n'):
                if line.strip():
                    try:
                        result = json.loads(line)

                        # Extract usage from response
                        if 'response' in result and 'body' in result['response']:
                            response_body = result['response']['body']
                            if 'usage' in response_body:
                                usage = response_body['usage']
                                prompt_tokens = usage.get('prompt_tokens', 0)
                                completion_tokens = usage.get('completion_tokens', 0)
                                total_request_tokens = usage.get('total_tokens', prompt_tokens + completion_tokens)

                                token_breakdown['prompt_tokens'] += prompt_tokens
                                token_breakdown['completion_tokens'] += completion_tokens
                                token_breakdown['total_tokens'] += total_request_tokens
                                total_tokens += total_request_tokens
                                request_count += 1

                                # Calculate cost (GPT-4o-mini pricing as of 2024)
                                # Input: $0.150 per 1M tokens, Output: $0.600 per 1M tokens
                                input_cost = (prompt_tokens / 1_000_000) * 0.150
                                output_cost = (completion_tokens / 1_000_000) * 0.600
                                total_cost += input_cost + output_cost

                    except json.JSONDecodeError:
                        continue

            # Calculate per-page averages
            avg_tokens_per_page = total_tokens / request_count if request_count > 0 else 0
            avg_cost_per_page = total_cost / request_count if request_count > 0 else 0

            usage_stats = {
                'batch_id': batch_id,
                'total_requests': request_count,
                'total_tokens': total_tokens,
                'total_cost': total_cost,
                'avg_tokens_per_page': avg_tokens_per_page,
                'avg_cost_per_page': avg_cost_per_page,
                'token_breakdown': token_breakdown,
                'cost_breakdown': {
                    'input_cost': (token_breakdown['prompt_tokens'] / 1_000_000) * 0.150,
                    'output_cost': (token_breakdown['completion_tokens'] / 1_000_000) * 0.600
                }
            }

            # Save usage stats to file
            usage_file = f"usage_stats_{batch_id}.json"
            with open(usage_file, 'w', encoding='utf-8') as f:
                json.dump(usage_stats, f, indent=2)

            self.print_status(f"Usage analysis saved to {usage_file}", "SUCCESS")
            return usage_stats

        except Exception as e:
            self.print_status(f"Error analyzing batch usage: {e}", "ERROR")
            return None

    def print_usage_summary(self, usage_stats):
        """Print a formatted usage summary"""
        if not usage_stats:
            return

        print("\n" + "="*60)
        print("📊 BATCH USAGE ANALYSIS")
        print("="*60)
        print(f"Batch ID: {usage_stats['batch_id']}")
        print(f"Total Requests: {usage_stats['total_requests']:,}")
        print(f"Total Tokens: {usage_stats['total_tokens']:,}")
        print(f"Total Cost: ${usage_stats['total_cost']:.4f}")
        print("\n📈 Per-Page Averages:")
        print(f"  Tokens per page: {usage_stats['avg_tokens_per_page']:.0f}")
        print(f"  Cost per page: ${usage_stats['avg_cost_per_page']:.4f}")
        print("\n🔢 Token Breakdown:")
        print(f"  Prompt tokens: {usage_stats['token_breakdown']['prompt_tokens']:,}")
        print(f"  Completion tokens: {usage_stats['token_breakdown']['completion_tokens']:,}")
        print(f"  Total tokens: {usage_stats['token_breakdown']['total_tokens']:,}")
        print("\n💰 Cost Breakdown:")
        print(f"  Input cost: ${usage_stats['cost_breakdown']['input_cost']:.4f}")
        print(f"  Output cost: ${usage_stats['cost_breakdown']['output_cost']:.4f}")
        print(f"  Total cost: ${usage_stats['total_cost']:.4f}")
        print("="*60)

    def retrieve_batch_results(self, batch_id):
        """Retrieve batch results and analyze usage"""
        self.print_status(f"Retrieving results for batch {batch_id}", "PROGRESS")

        try:
            result = subprocess.run([
                sys.executable, "batch_api.py", "retrieve", batch_id
            ], capture_output=True, text=True, encoding='utf-8', errors='replace')

            if result.returncode == 0:
                self.print_status("Results retrieved successfully", "SUCCESS")

                # Analyze usage and costs
                usage_stats = self.analyze_batch_usage(batch_id)
                if usage_stats:
                    self.print_usage_summary(usage_stats)

                return True
            else:
                self.print_status(f"Failed to retrieve results: {result.stderr}", "ERROR")
                return False

        except Exception as e:
            self.print_status(f"Error retrieving results: {e}", "ERROR")
            return False

    def find_active_batches(self):
        """Find all active batch files"""
        batch_files = list(Path(".").glob("batch_info_*.json"))
        active_batches = []

        for batch_file in batch_files:
            try:
                batch_id = batch_file.name.replace("batch_info_", "").replace(".json", "")
                status_info = self.check_batch_status(batch_id)
                if status_info:
                    active_batches.append(status_info)
            except Exception as e:
                self.print_status(f"Error processing {batch_file}: {e}", "WARNING")

        return active_batches

    def monitor_batches(self, check_interval=30, max_iterations=None):
        """Monitor all active batches"""
        self.print_status("Starting batch monitoring", "INFO")
        iterations = 0

        while True:
            if max_iterations and iterations >= max_iterations:
                self.print_status("Maximum iterations reached", "INFO")
                break

            iterations += 1
            self.print_status(f"Check #{iterations} - Monitoring active batches...", "PROGRESS")

            active_batches = self.find_active_batches()

            if not active_batches:
                self.print_status("No active batches found", "INFO")
                break

            completed_batches = []

            for batch_info in active_batches:
                batch_id = batch_info['id']
                status = batch_info['status']
                completed = batch_info['completed']
                total = batch_info['total']

                self.print_status(f"Batch {batch_id}: {status} ({completed}/{total})", "INFO")

                if status == "completed":
                    completed_batches.append(batch_id)
                elif status == "failed":
                    self.print_status(f"Batch {batch_id} failed!", "ERROR")
                elif status in ["in_progress", "validating", "finalizing"]:
                    continue
                else:
                    self.print_status(f"Unknown status for batch {batch_id}: {status}", "WARNING")

            # Retrieve results for completed batches
            for batch_id in completed_batches:
                self.print_status(f"Processing completed batch: {batch_id}", "SUCCESS")
                self.retrieve_batch_results(batch_id)

            # Check if all batches are done
            remaining_batches = [b for b in active_batches if b['status'] not in ['completed', 'failed']]

            if not remaining_batches:
                self.print_status("All batches completed!", "SUCCESS")
                break

            if not max_iterations:  # Only sleep if running continuously
                self.print_status(f"Waiting {check_interval} seconds before next check...", "INFO")
                time.sleep(check_interval)

    def create_master_document(self):
        """Create a master document combining all batch results"""
        self.print_status("Creating master document from all batch results", "PROGRESS")

        converted_dir = Path("converted")
        if not converted_dir.exists():
            self.print_status("No converted directory found", "WARNING")
            return False

        batch_files = list(converted_dir.glob("*_batch.md"))
        if not batch_files:
            self.print_status("No batch result files found", "WARNING")
            return False

        # Group files by PDF name
        pdf_groups = {}
        for batch_file in batch_files:
            pdf_name = batch_file.stem.replace("_batch", "")
            pdf_groups[pdf_name] = batch_file

        master_content = []
        master_content.append("# CAN-RS485 Documentation Master Collection\n")
        master_content.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        master_content.append(f"Total Documents: {len(pdf_groups)}\n\n")

        # Add table of contents
        master_content.append("## Table of Contents\n")
        for i, pdf_name in enumerate(sorted(pdf_groups.keys()), 1):
            title = pdf_name.replace("-", " ").replace("_", " ").title()
            master_content.append(f"{i}. [{title}](#{pdf_name.lower()})\n")
        master_content.append("\n---\n\n")

        # Add each document
        for pdf_name in sorted(pdf_groups.keys()):
            batch_file = pdf_groups[pdf_name]
            title = pdf_name.replace("-", " ").replace("_", " ").title()

            master_content.append(f"# {title} {{#{pdf_name.lower()}}}\n\n")

            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Remove the individual metadata section
                    content = content.split("## Processing Metadata")[0]
                    master_content.append(content)
                    master_content.append("\n\n---\n\n")

            except Exception as e:
                self.print_status(f"Error reading {batch_file}: {e}", "ERROR")
                master_content.append(f"*Error reading {pdf_name}: {e}*\n\n")

        # Add master metadata
        master_content.append("## Master Document Metadata\n\n")
        master_content.append(f"- **Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        master_content.append(f"- **Source Method:** OpenAI Batch API\n")
        master_content.append(f"- **Model:** {self.model}\n")
        master_content.append(f"- **Documents Included:** {len(pdf_groups)}\n")
        master_content.append(f"- **Individual Files:** {', '.join(sorted(pdf_groups.keys()))}\n")

        # Write master file
        master_file = "CAN_RS485_Master_Documentation.md"
        try:
            with open(master_file, 'w', encoding='utf-8') as f:
                f.writelines(master_content)

            # Get file size
            file_size = os.path.getsize(master_file)
            self.print_status(f"Master document created: {master_file} ({file_size:,} bytes)", "SUCCESS")
            return True

        except Exception as e:
            self.print_status(f"Error creating master document: {e}", "ERROR")
            return False

    def cleanup_temp_files(self):
        """Clean up temporary files and directories"""
        self.print_status("Cleaning up temporary files", "PROGRESS")

        cleanup_patterns = [
            "batch_requests_*.jsonl",
            "temp_batch",
            "batch_info_*.json"
        ]

        cleaned = 0
        for pattern in cleanup_patterns:
            if "*" in pattern:
                # Glob pattern
                for item in Path(".").glob(pattern):
                    try:
                        if item.is_dir():
                            shutil.rmtree(item)
                        else:
                            item.unlink()
                        cleaned += 1
                    except Exception as e:
                        self.print_status(f"Could not remove {item}: {e}", "WARNING")
            else:
                # Direct path
                item = Path(pattern)
                if item.exists():
                    try:
                        if item.is_dir():
                            shutil.rmtree(item)
                        else:
                            item.unlink()
                        cleaned += 1
                    except Exception as e:
                        self.print_status(f"Could not remove {item}: {e}", "WARNING")

        self.print_status(f"Cleaned up {cleaned} items", "SUCCESS")

    def run_complete_workflow(self):
        """Run the complete batch processing workflow"""
        self.print_status("Starting complete PDF batch processing workflow", "SUCCESS")

        # Step 1: Check for existing batches
        existing_batches = self.find_active_batches()
        if existing_batches:
            self.print_status(f"Found {len(existing_batches)} existing batches", "INFO")
            for batch in existing_batches:
                self.print_status(f"  - {batch['id']}: {batch['status']} ({batch['completed']}/{batch['total']})", "INFO")

        # Step 2: Submit new batch if no active ones
        if not existing_batches or all(b['status'] in ['completed', 'failed'] for b in existing_batches):
            batch_id = self.submit_new_batch()
            if not batch_id:
                self.print_status("Failed to submit new batch", "ERROR")
                return False

        # Step 3: Monitor until completion
        self.monitor_batches(check_interval=30)

        # Step 4: Create master document
        self.create_master_document()

        # Step 5: Optional cleanup
        response = input("\nClean up temporary files? (y/N): ").strip().lower()
        if response == 'y':
            self.cleanup_temp_files()

        self.print_status("Complete workflow finished!", "SUCCESS")
        return True

def main():
    master = PDFBatchMaster()

    if len(sys.argv) < 2:
        print("PDF Batch Master - Complete batch processing management")
        print("\nUsage:")
        print("  python master.py workflow          # Run complete workflow")
        print("  python master.py submit            # Submit new batch")
        print("  python master.py monitor [seconds] # Monitor active batches")
        print("  python master.py master            # Create master document")
        print("  python master.py status            # Show all batch statuses")
        print("  python master.py usage [batch_id]  # Analyze usage and costs")
        print("  python master.py cleanup           # Clean up temp files")
        return

    command = sys.argv[1].lower()

    if command == "workflow":
        master.run_complete_workflow()

    elif command == "submit":
        batch_id = master.submit_new_batch()
        if batch_id:
            print(f"\nBatch submitted: {batch_id}")
            print(f"Monitor with: python master.py monitor")

    elif command == "monitor":
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 30
        master.monitor_batches(check_interval=interval)

    elif command == "master":
        master.create_master_document()

    elif command == "status":
        batches = master.find_active_batches()
        if batches:
            print(f"\nFound {len(batches)} batches:")
            for batch in batches:
                print(f"  {batch['id']}: {batch['status']} ({batch['completed']}/{batch['total']})")
        else:
            print("No active batches found")

    elif command == "usage":
        if len(sys.argv) > 2:
            batch_id = sys.argv[2]
            usage_stats = master.analyze_batch_usage(batch_id)
            if usage_stats:
                master.print_usage_summary(usage_stats)
        else:
            # Analyze all completed batches
            batches = master.find_active_batches()
            completed_batches = [b for b in batches if b['status'] == 'completed']
            if completed_batches:
                total_cost = 0
                total_tokens = 0
                total_pages = 0

                for batch in completed_batches:
                    usage_stats = master.analyze_batch_usage(batch['id'])
                    if usage_stats:
                        master.print_usage_summary(usage_stats)
                        total_cost += usage_stats['total_cost']
                        total_tokens += usage_stats['total_tokens']
                        total_pages += usage_stats['total_requests']

                if total_pages > 0:
                    print(f"\n{'='*60}")
                    print("📊 TOTAL USAGE SUMMARY")
                    print(f"{'='*60}")
                    print(f"Total batches analyzed: {len(completed_batches)}")
                    print(f"Total pages processed: {total_pages:,}")
                    print(f"Total tokens used: {total_tokens:,}")
                    print(f"Total cost: ${total_cost:.4f}")
                    print(f"Average cost per page: ${total_cost/total_pages:.4f}")
                    print(f"{'='*60}")
            else:
                print("No completed batches found for usage analysis")

    elif command == "cleanup":
        master.cleanup_temp_files()

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
