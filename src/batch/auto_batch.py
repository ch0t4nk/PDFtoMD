"""
Auto Batch PDF Converter - Fully Automated PDF to Markdown Conversion.

Usage: python auto_batch.py [pdf_folder] [output_folder] [options]
"""

import argparse
import importlib.util
import json
import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

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

# Handle imports whether running as module or script
try:
    from .batch_api import BatchPDFConverter
    from .master import PDFBatchMaster
except ImportError:
    # Running as script, add parent directory to path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from batch.batch_api import BatchPDFConverter
    from batch.master import PDFBatchMaster


class AutoBatchProcessor:
    """Automated batch PDF processing with SSOT configuration compliance."""

    def __init__(self, pdf_folder=None, output_folder=None, enable_linting=True, prompt_type="batch"):
        self.pdf_folder = (
            Path(pdf_folder) if pdf_folder else Path(str(config.DEFAULT_PDF_FOLDER))
        )
        self.output_folder = (
            Path(output_folder)
            if output_folder
            else Path(str(config.DEFAULT_OUTPUT_FOLDER))
        )
        self.enable_linting = enable_linting
        self.master = PDFBatchMaster()
        self.converter = BatchPDFConverter(prompt_type=prompt_type)
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.prompt_type = prompt_type

    def print_banner(self, message, symbol="="):
        """Print formatted banner"""
        print(f"\n{symbol * 60}")
        print(f"🤖 {message}")
        print(f"{symbol * 60}")

    def print_step(self, step, message):
        """Print step information"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"⏰ [{timestamp}] Step {step}: {message}")

    def discover_pdfs(self):
        """Discover all PDF files in the input folder"""
        self.print_step(1, f"Scanning for PDFs in {self.pdf_folder}")

        if not self.pdf_folder.exists():
            raise FileNotFoundError(f"PDF folder not found: {self.pdf_folder}")

        pdf_files = list(self.pdf_folder.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(f"No PDF files found in {self.pdf_folder}")

        print(f"✅ Found {len(pdf_files)} PDF files:")
        for pdf in pdf_files:
            # Get file size
            size_mb = pdf.stat().st_size / (1024 * 1024)
            print(f"   📄 {pdf.name} ({size_mb:.1f} MB)")

        return pdf_files

    def setup_workspace(self, pdf_files):
        """Setup workspace for batch processing"""
        self.print_step(2, "Setting up workspace")

        # Create output directory
        self.output_folder.mkdir(exist_ok=True, parents=True)

        # Create session folder for this run
        session_folder = self.output_folder / f"session_{self.session_id}"
        session_folder.mkdir(exist_ok=True)

        # Create temporary pdfs folder if needed
        temp_pdfs = Path(str(config.DEFAULT_PDF_FOLDER))
        if not temp_pdfs.exists() or temp_pdfs != self.pdf_folder:
            temp_pdfs.mkdir(exist_ok=True)
            # Copy PDFs to workspace
            print("📂 Copying PDFs to workspace...")
            for pdf_file in pdf_files:
                dest = temp_pdfs / pdf_file.name
                if not dest.exists():
                    shutil.copy2(pdf_file, dest)
                    print(f"   ✅ Copied {pdf_file.name}")

        print(f"✅ Workspace ready: {session_folder}")
        return session_folder

    def estimate_costs(self, pdf_files):
        """Estimate processing costs"""
        self.print_step(3, "Estimating processing costs")

        total_size_mb = sum(pdf.stat().st_size for pdf in pdf_files) / (1024 * 1024)

        # Rough estimates based on previous runs
        estimated_pages = int(total_size_mb * 0.8)  # ~0.8 pages per MB average
        estimated_tokens = estimated_pages * 31000  # ~31k tokens per page
        estimated_cost = (
            estimated_tokens * (0.150 / 1_000_000) * 1.1
        )  # Input cost + small output cost

        print("📊 Processing Estimates:")
        print(f"   📄 Files: {len(pdf_files)}")
        print(f"   📦 Total Size: {total_size_mb:.1f} MB")
        print(f"   📃 Estimated Pages: ~{estimated_pages}")
        print(f"   🔢 Estimated Tokens: ~{estimated_tokens:,}")
        print(f"   💰 Estimated Cost: ~${estimated_cost:.2f}")
        print("   ⏱️  Estimated Time: 5-15 minutes")

        return {
            "files": len(pdf_files),
            "size_mb": total_size_mb,
            "estimated_pages": estimated_pages,
            "estimated_tokens": estimated_tokens,
            "estimated_cost": estimated_cost,
        }

    def submit_batch(self):
        """Submit batch for processing with error handling"""
        self.print_step(4, "Submitting batch to OpenAI")

        # Use batch_api to submit
        pdf_dir = Path(str(config.DEFAULT_PDF_FOLDER))
        pdf_files = [f.name for f in pdf_dir.glob("*.pdf")]

        requests, file_mapping = self.converter.create_batch_requests(pdf_files)
        batch_id = self.converter.submit_batch(requests, file_mapping)

        if batch_id is None:
            print(f"\n❌ BATCH SUBMISSION FAILED")
            print(f"   Unable to submit batch to OpenAI.")
            print(f"   Please resolve the issues above and try again.")
            return None

        print(f"✅ Batch submitted: {batch_id}")
        print(f"📊 Requests queued: {len(requests)}")

        return batch_id

    def monitor_batch(self, batch_id):
        """Monitor batch until completion (handles both single and chunked batches)"""
        self.print_step(5, f"Monitoring batch {batch_id}")

        start_time = time.time()
        check_count = 0

        while True:
            check_count += 1
            elapsed = time.time() - start_time

            print(
                f"⏰ [{time.strftime('%H:%M:%S')}] Check #{check_count} - {elapsed / 60:.1f}m elapsed"
            )

            # Use the batch_api to check status (handles chunked batches automatically)
            status_result = self.converter.check_batch_status(batch_id)

            if not status_result:
                print("❌ Batch not found!")
                return False

            # Handle chunked batch results
            if isinstance(status_result, dict) and "master_batch_id" in status_result:
                # Chunked batch
                completed_requests = status_result.get("completed_requests", 0)
                total_requests = status_result.get("total_requests", 0)
                completed_chunks = status_result.get("completed_chunks", 0)
                total_chunks = status_result.get("total_chunks", 0)
                all_completed = status_result.get("all_completed", False)
                any_failed = status_result.get("any_failed", False)

                if total_requests > 0:
                    progress_pct = (completed_requests / total_requests) * 100
                    print(
                        f"   📊 Progress: {completed_requests}/{total_requests} requests ({progress_pct:.1f}%)"
                    )
                    print(f"   📦 Chunks: {completed_chunks}/{total_chunks} completed")

                if all_completed:
                    print(f"✅ All chunks completed in {elapsed / 60:.1f} minutes!")
                    return True
                elif any_failed and completed_chunks == 0:
                    print("❌ All chunks failed!")
                    return False
                elif any_failed and completed_chunks > 0:
                    print(
                        f"⚠️  Some chunks failed, but {completed_chunks}/{total_chunks} completed successfully"
                    )
                    print(
                        f"   📊 Partial success: {completed_requests}/{total_requests} requests completed ({(completed_requests / total_requests) * 100:.1f}%)"
                    )
                    # If we have significant completion, consider it a partial success
                    if (
                        completed_requests > total_requests * 0.5
                    ):  # More than 50% completed
                        print("✅ Continuing with partial results (>50% completion)")
                        return True
                    else:
                        print("❌ Too many failures, aborting")
                        return False
                else:
                    # Still processing
                    time.sleep(30)
                    continue

            else:
                # Single batch (batch object from OpenAI API)
                try:
                    if hasattr(status_result, "status"):
                        status = status_result.status
                        request_counts = status_result.request_counts

                        if request_counts:
                            completed = getattr(request_counts, "completed", 0) or 0
                            total = getattr(request_counts, "total", 0) or 0
                            progress_pct = (completed / total * 100) if total > 0 else 0
                            print(
                                f"   📊 Status: {status} ({completed}/{total} - {progress_pct:.1f}%)"
                            )
                        else:
                            print(f"   📊 Status: {status}")

                        if status == "completed":
                            print(f"✅ Batch completed in {elapsed / 60:.1f} minutes!")
                            return True
                        elif status == "failed":
                            print("❌ Batch failed!")
                            return False
                        else:
                            # Still processing
                            time.sleep(30)
                            continue
                    else:
                        # Unexpected result type
                        print(f"❌ Unexpected status result: {status_result}")
                        return False
                except AttributeError:
                    # Handle case where status_result doesn't have expected attributes
                    print(f"❌ Invalid status result format: {type(status_result)}")
                    return False

    def retrieve_results(self, batch_id):
        """Retrieve and process results"""
        self.print_step(6, "Retrieving results and generating files")

        # Retrieve results using batch_api
        success = self.converter.retrieve_results(batch_id)

        if not success:
            print("❌ Failed to retrieve results")
            return False

        print("✅ Results retrieved successfully")
        return True

    def apply_linting(self):
        """Apply linting to converted files if enabled"""
        if not self.enable_linting:
            self.print_step("7a", "Skipping linting (disabled)")
            return None

        self.print_step("7a", "Applying markdown linting to converted files")

        try:
            # Try to import linting functionality
            try:
                from src.utils.linting.markdown_linter import MarkdownLinter

                linter = MarkdownLinter()
            except ImportError:
                print("⚠️  Markdown linter not available, skipping linting")
                return {}
            converted_dir = Path(str(config.DEFAULT_CONVERTED_FOLDER))

            if not converted_dir.exists():
                print("⚠️  No converted directory found, skipping linting")
                return None

            # Get all markdown files
            md_files = list(converted_dir.glob("*.md"))
            if not md_files:
                print("⚠️  No markdown files found, skipping linting")
                return None

            total_fixes = 0
            total_size_reduction = 0
            files_processed = 0

            print(f"🔧 Linting {len(md_files)} files...")

            for md_file in md_files:
                if "_batch.md" in md_file.name:  # Only lint batch files
                    result = linter.lint_file(str(md_file))

                    if "error" not in result:
                        fixes_applied = len(result.get("fixes", []))
                        size_reduction = result.get("size_reduction", 0)

                        total_fixes += fixes_applied
                        total_size_reduction += size_reduction
                        files_processed += 1

                        if fixes_applied > 0:
                            print(
                                f"   ✅ {md_file.name}: {fixes_applied} fixes, {size_reduction} bytes saved"
                            )
                        else:
                            print(f"   ✅ {md_file.name}: Already clean")
                    else:
                        print(f"   ❌ {md_file.name}: {result['error']}")

            linting_stats = {
                "total_fixes": total_fixes,
                "total_size_reduction": total_size_reduction,
                "files_processed": files_processed,
                "avg_fixes_per_file": total_fixes / max(files_processed, 1),
                "avg_size_reduction": total_size_reduction / max(files_processed, 1),
            }

            print(
                f"✅ Linting complete: {total_fixes} total fixes, {total_size_reduction:,} bytes saved"
            )
            return linting_stats

        except ImportError:
            print("⚠️  Linting module not available, skipping")
            return None
        except (OSError, RuntimeError, ValueError) as e:
            print(f"⚠️  Linting failed: {e}")
            return None

    def enhance_with_metadata(self, report, linting_stats):
        """Add metadata headers and session summaries to converted files"""
        if not report:
            print("⚠️  No report data available, skipping metadata enhancement")
            return

        self.print_step("7c", "Adding metadata to converted files")

        try:
            try:
                from src.utils.metadata_embedder import enhance_converted_files
            except ImportError:
                print(
                    "⚠️  Metadata embedder not available, skipping metadata enhancement"
                )
                return

            # Prepare batch data for metadata enhancement
            batch_data = {
                "session_id": self.session_id,
                "batch_id": report.get("batch_id"),
                "total_cost": report.get("actual_results", {}).get("total_cost", 0),
                "total_files": report.get("actual_results", {}).get(
                    "total_requests", 0
                ),
                "total_pages": report.get("actual_results", {}).get("total_pages", 0),
                "session_start": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),  # Approximate
                "session_end": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "files": [],
            }

            # Add file details if available
            if "file_details" in report:
                for file_detail in report["file_details"]:
                    batch_data["files"].append(
                        {
                            "name": file_detail.get("file", "unknown.pdf"),
                            "pages": file_detail.get("pages", 0),
                            "cost": file_detail.get("cost", 0),
                            "cost_per_page": file_detail.get("cost_per_page", 0),
                            "tokens": file_detail.get("tokens", 0),
                            "final_size": file_detail.get("final_size", "unknown"),
                        }
                    )

            # Apply metadata enhancement
            enhance_converted_files(
                str(config.DEFAULT_CONVERTED_FOLDER), batch_data, linting_stats
            )

            print("✅ Metadata enhancement completed")

        except ImportError:
            print("⚠️  Metadata enhancement module not available, skipping")
        except (RuntimeError, OSError, ValueError) as e:
            print(f"⚠️  Metadata enhancement failed: {e}")

    def analyze_costs(self, batch_id, estimates):
        """Analyze final costs and compare to estimates"""
        self.print_step("7b", "Analyzing costs and generating report")

        # Get usage statistics
        usage_stats = self.master.analyze_batch_usage(batch_id)

        if not usage_stats:
            print("⚠️  Could not retrieve usage statistics")
            return None

        # Compare to estimates
        actual_cost = usage_stats["total_cost"]
        estimated_cost = estimates["estimated_cost"]
        cost_diff = actual_cost - estimated_cost
        cost_diff_pct = (cost_diff / estimated_cost * 100) if estimated_cost > 0 else 0

        report = {
            "session_id": self.session_id,
            "batch_id": batch_id,
            "timestamp": datetime.now().isoformat(),
            "estimates": estimates,
            "actual_results": usage_stats,
            "comparison": {
                "cost_difference": cost_diff,
                "cost_difference_pct": cost_diff_pct,
                "pages_difference": usage_stats["total_requests"]
                - estimates["estimated_pages"],
                "tokens_difference": usage_stats["total_tokens"]
                - estimates["estimated_tokens"],
            },
        }

        print("\n📊 COST ANALYSIS SUMMARY")
        print("=" * 50)
        print(f"💰 Estimated Cost: ${estimated_cost:.4f}")
        print(f"💰 Actual Cost: ${actual_cost:.4f}")
        print(f"💰 Difference: ${cost_diff:+.4f} ({cost_diff_pct:+.1f}%)")
        print(f"📄 Pages Processed: {usage_stats['total_requests']}")
        print(f"🔢 Tokens Used: {usage_stats['total_tokens']:,}")
        print(f"⚡ Cost per Page: ${usage_stats['avg_cost_per_page']:.4f}")
        print(f"{'=' * 50}")

        return report

    def organize_outputs(self, session_folder, report):
        """Organize final outputs"""
        self.print_step(8, "Organizing final outputs")

        # Move converted files to session folder
        converted_dir = Path(str(config.DEFAULT_CONVERTED_FOLDER))
        if converted_dir.exists():
            session_converted = session_folder / "markdown_files"
            session_converted.mkdir(exist_ok=True)

            for md_file in converted_dir.glob("*.md"):
                dest = session_converted / md_file.name
                shutil.move(str(md_file), str(dest))
                print(f"   📝 Moved {md_file.name}")

        # Save cost report
        if report:
            report_file = session_folder / "cost_analysis.json"
            with open(report_file, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2)
            print(f"   📊 Saved cost analysis: {report_file}")

        # Create summary file
        summary_file = session_folder / "README.md"
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(f"# Batch Processing Session {self.session_id}\n\n")
            f.write("## Summary\n")
            f.write(f"- **Session ID:** {self.session_id}\n")
            f.write(
                f"- **Processed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            if report:
                f.write(f"- **Batch ID:** {report['batch_id']}\n")
                f.write(
                    f"- **Files Processed:** {report['actual_results']['total_requests']}\n"
                )
                f.write(
                    f"- **Total Cost:** ${report['actual_results']['total_cost']:.4f}\n"
                )
                f.write(
                    f"- **Average Cost per Page:** ${report['actual_results']['avg_cost_per_page']:.4f}\n"
                )
            f.write("\n## Contents\n")
            f.write("- `markdown_files/` - Converted markdown documents\n")
            f.write("- `cost_analysis.json` - Detailed cost breakdown\n")
            f.write("- `README.md` - This summary file\n")

        print(f"✅ Session organized: {session_folder}")
        return session_folder

    def cleanup_workspace(self):
        """Clean up temporary files"""
        print("\n🧹 Cleaning up workspace...")

        # Remove temp files but keep pdfs if they were copied
        # NOTE: Only clean up files in the working directory, NOT the output folder
        cleanup_patterns = [
            "temp_batch",
            "batch_info_*.json",
            "usage_stats_*.json",
        ]

        # Only clean converted folder if it's in the workspace (not the target output)
        converted_dir = Path(str(config.DEFAULT_CONVERTED_FOLDER))
        if converted_dir.is_relative_to(Path.cwd()):
            cleanup_patterns.append(str(converted_dir))

        # Also clean up temp directory contents and stray page images
        temp_cleanup_patterns = [
            "temp/workspace/*",
            "temp/output/*",
            "temp/temp_batch",
            "page_*.jpg",  # Page images that may have been created in root (legacy issue)
            "*.jpg",  # Individual page images in root (legacy issue)
        ]

        cleaned = 0

        # Clean up main patterns (only in current working directory)
        for pattern in cleanup_patterns:
            if "*" in pattern:
                for item in Path(".").glob(pattern):
                    # Safety check: don't delete session folders
                    if "session_" in item.name:
                        print(f"   ⚠️  Skipped session folder: {item.name}")
                        continue
                    try:
                        if item.is_dir():
                            shutil.rmtree(item)
                            print("   🗑️  Removed temp batch directory")
                        else:
                            item.unlink()
                            print(f"   🗑️  Removed {item.name}")
                        cleaned += 1
                    except (OSError, PermissionError):
                        pass
            else:
                item = Path(pattern)
                if item.exists() and "session_" not in item.name:
                    try:
                        if item.is_dir():
                            shutil.rmtree(item)
                            print("   🗑️  Cleaned converted directory")
                        else:
                            item.unlink()
                        cleaned += 1
                    except (OSError, PermissionError):
                        pass

        # Clean up temp directory patterns
        for pattern in temp_cleanup_patterns:
            for item in Path(".").glob(pattern):
                # Additional safety check for session folders
                if "session_" in str(item):
                    print(f"   ⚠️  Skipped session-related file: {item}")
                    continue
                try:
                    if item.is_dir():
                        shutil.rmtree(item)
                        print(f"   🗑️  Removed temp directory: {item}")
                    else:
                        item.unlink()
                        print(f"   🗑️  Removed temp file: {item.name}")
                    cleaned += 1
                except (OSError, PermissionError):
                    pass

        print(f"✅ Cleaned up {cleaned} temporary items")

    def run_full_automation(self):
        """Run the complete automated process"""
        start_time = time.time()

        self.print_banner("AUTOMATED BATCH PDF PROCESSING", "🚀")
        print(f"📁 Input Folder: {self.pdf_folder}")
        print(f"📁 Output Folder: {self.output_folder}")
        print(f"🆔 Session ID: {self.session_id}")

        try:
            # Step 1: Discover PDFs
            pdf_files = self.discover_pdfs()

            # Step 2: Setup workspace
            session_folder = self.setup_workspace(pdf_files)

            # Step 3: Estimate costs
            estimates = self.estimate_costs(pdf_files)

            # Step 4: Submit batch
            batch_id = self.submit_batch()
            if batch_id is None:
                raise RuntimeError(
                    "Batch submission failed - check OpenAI account status"
                )

            # Step 5: Monitor batch
            if not self.monitor_batch(batch_id):
                raise RuntimeError("Batch processing failed")

            # Step 6: Retrieve results
            if not self.retrieve_results(batch_id):
                raise RuntimeError("Failed to retrieve results")

            # Step 7a: Apply linting (if enabled)
            linting_stats = self.apply_linting()

            # Step 7b: Analyze costs
            report = self.analyze_costs(batch_id, estimates)

            # Step 7c: Apply metadata enhancement
            self.enhance_with_metadata(report, linting_stats)

            # Step 8: Organize outputs
            final_folder = self.organize_outputs(session_folder, report)

            # Step 9: Cleanup (only if enabled)
            if config.AUTO_CLEANUP:
                self.cleanup_workspace()
            else:
                print("\n🚫 Auto cleanup disabled - temporary files preserved")

            # Final summary
            total_time = time.time() - start_time
            self.print_banner("PROCESSING COMPLETE! 🎉", "✅")
            print(f"⏱️  Total Time: {total_time / 60:.1f} minutes")
            print(f"📁 Results: {final_folder}")
            if report:
                print(f"💰 Total Cost: ${report['actual_results']['total_cost']:.4f}")
                print(
                    f"📄 Files Processed: {report['actual_results']['total_requests']}"
                )
            print("✅ Ready to use!")

            return True

        except (RuntimeError, OSError, ValueError, TypeError) as e:
            self.print_banner("PROCESSING FAILED ❌", "❌")
            print(f"Error: {e}")
            print("Manual cleanup may be required.")
            return False


def main():
    """Main entry point with proper argument parsing"""
    parser = argparse.ArgumentParser(
        description="🤖 Auto Batch PDF Converter - Fully Automated PDF to Markdown Conversion",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python auto_batch.py                          # Use default folders
  python auto_batch.py pdfs                     # Specify input folder
  python auto_batch.py pdfs output --no-lint    # Skip linting step
  python auto_batch.py /path/to/pdfs /path/to/output

Safety:
  ⚠️  Original PDF files are NEVER deleted or modified
  This tool only creates new .md files and cleans temporary processing files
""",
    )

    parser.add_argument(
        "pdf_folder",
        nargs="?",
        default=str(config.DEFAULT_PDF_FOLDER),
        help=f"Input folder containing PDF files (default: {config.DEFAULT_PDF_FOLDER})",
    )
    parser.add_argument(
        "output_folder",
        nargs="?",
        default=str(config.DEFAULT_OUTPUT_FOLDER),
        help=f"Output folder for converted files (default: {config.DEFAULT_OUTPUT_FOLDER})",
    )
    parser.add_argument(
        "--no-lint",
        "--skip-lint",
        action="store_true",
        help="Skip the markdown linting step (faster processing)",
    )
    parser.add_argument(
        "--no-metadata",
        action="store_true",
        help="Skip metadata enhancement (embedded headers and summaries)",
    )
    parser.add_argument(
        "--prompt-type",
        choices=["batch", "mermaid"],
        default="batch",
        help="Type of prompts to use: 'batch' for standard processing or 'mermaid' for enhanced diagrams (default: batch)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Show configuration
    print("🤖 Auto Batch PDF Converter")
    print(f"📁 Input Folder: {args.pdf_folder}")
    print(f"📁 Output Folder: {args.output_folder}")
    print(f"🔧 Linting: {'Disabled' if args.no_lint else 'Enabled'}")
    print(f"📊 Metadata: {'Disabled' if args.no_metadata else 'Enabled'}")
    print(f"🎨 Prompt Type: {args.prompt_type.upper()}")
    print()

    print("This script will:")
    print("  1. 🔍 Scan for PDFs in the input folder")
    print("  2. 📊 Estimate processing costs")
    print("  3. 🚀 Submit batch to OpenAI")
    print("  4. ⏰ Monitor progress automatically")
    print("  5. 📥 Retrieve results when complete")
    if not args.no_lint:
        print("  6. 🔧 Apply markdown linting")
    if not args.no_metadata:
        print("  7. 📊 Add metadata headers and session summaries")
    print("  8. 💰 Generate cost analysis")
    print("  9. 📁 Organize outputs in timestamped session folder")
    print("  10. 🧹 Clean up temporary files")
    print()

    # Run automation
    processor = AutoBatchProcessor(
        pdf_folder=args.pdf_folder,
        output_folder=args.output_folder,
        enable_linting=not args.no_lint,
        prompt_type=args.prompt_type,
    )
    success = processor.run_full_automation()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
