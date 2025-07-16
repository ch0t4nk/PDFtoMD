#!/usr/bin/env python3
"""
Auto Batch PDF Converter - Fully Automated PDF to Markdown Conversion
Usage: python auto_batch.py [pdf_folder] [output_folder] [options]
"""

import os
import sys
import time
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Any, Optional

# Add root directory to path for config import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import importlib.util

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
    from ..batch.master import PDFBatchMaster
    from ..batch.batch_api import BatchPDFConverter
except ImportError:
    # Running as script, add src directory to path
    src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, src_dir)
    from batch.master import PDFBatchMaster
    from batch.batch_api import BatchPDFConverter

class AutoBatchProcessor:
    def __init__(self, pdf_folder=None, output_folder=None, enable_linting=True):
        self.pdf_folder = Path(pdf_folder) if pdf_folder else Path(str(config.DEFAULT_PDF_FOLDER))
        self.output_folder = Path(output_folder) if output_folder else Path(str(config.DEFAULT_CONVERTED_FOLDER))
        self.enable_linting = enable_linting
        self.master = PDFBatchMaster()
        self.converter = BatchPDFConverter()
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    def print_banner(self, message, symbol="="):
        """Print formatted banner"""
        print(f"\n{symbol * 60}")
        print(f"🤖 {message}")
        print(f"{symbol * 60}")

    def print_step(self, step, message):
        """Print step information"""
        timestamp = datetime.now().strftime('%H:%M:%S')
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
        estimated_cost = estimated_tokens * (0.150 / 1_000_000) * 1.1  # Input cost + small output cost

        print(f"📊 Processing Estimates:")
        print(f"   📄 Files: {len(pdf_files)}")
        print(f"   📦 Total Size: {total_size_mb:.1f} MB")
        print(f"   📃 Estimated Pages: ~{estimated_pages}")
        print(f"   🔢 Estimated Tokens: ~{estimated_tokens:,}")
        print(f"   💰 Estimated Cost: ~${estimated_cost:.2f}")
        print(f"   ⏱️  Estimated Time: 5-15 minutes")

        return {
            "files": len(pdf_files),
            "size_mb": total_size_mb,
            "estimated_pages": estimated_pages,
            "estimated_tokens": estimated_tokens,
            "estimated_cost": estimated_cost
        }

    def submit_batch(self):
        """Submit batch for processing"""
        self.print_step(4, "Submitting batch to OpenAI")

        # Use batch_api to submit
        pdf_dir = Path(str(config.DEFAULT_PDF_FOLDER))
        pdf_files = [f.name for f in pdf_dir.glob("*.pdf")]

        requests, file_mapping = self.converter.create_batch_requests(pdf_files)
        batch_id = self.converter.submit_batch(requests, file_mapping)

        print(f"✅ Batch submitted: {batch_id}")
        print(f"📊 Requests queued: {len(requests)}")

        return batch_id

    def monitor_batch(self, batch_id):
        """Monitor batch until completion"""
        self.print_step(5, f"Monitoring batch {batch_id}")

        start_time = time.time()
        check_count = 0

        while True:
            check_count += 1

            # Get batch status
            batches = self.master.find_active_batches()
            current_batch = None

            for batch in batches:
                if batch['id'] == batch_id:
                    current_batch = batch
                    break

            if not current_batch:
                print("❌ Batch not found!")
                return False

            status = current_batch['status']
            completed = current_batch['completed']
            total = current_batch['total']

            elapsed = time.time() - start_time
            progress_pct = (completed / total * 100) if total > 0 else 0

            print(f"   🔄 Check #{check_count}: {status} ({completed}/{total} - {progress_pct:.1f}%) - {elapsed/60:.1f}m elapsed")

            if status == "completed":
                print(f"✅ Batch completed in {elapsed/60:.1f} minutes!")
                return True
            elif status == "failed":
                print("❌ Batch failed!")
                return False
            else:
                # Wait before next check
                time.sleep(30)

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
            # Try to import linting functionality dynamically
            import importlib.util
            utils_dir = Path(__file__).parent.parent / "utils"
            linter_path = utils_dir / "linting" / "markdown_linter.py"

            linter = None
            if linter_path.exists() and linter_path.stat().st_size > 0:
                try:
                    spec = importlib.util.spec_from_file_location("markdown_linter", linter_path)
                    if spec and spec.loader:
                        linter_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(linter_module)

                        # Use getattr with try-except to handle dynamic instantiation
                        if hasattr(linter_module, 'MarkdownLinter'):
                            try:
                                linter = getattr(linter_module, 'MarkdownLinter')()
                                # Test if the linter has the required method
                                if not hasattr(linter, 'lint_file'):
                                    linter = None
                            except (TypeError, AttributeError, RuntimeError, ImportError):
                                linter = None
                except (TypeError, AttributeError, ImportError, RuntimeError):
                    linter = None

            if not linter:
                print("⚠️  Markdown linter not available, skipping linting")
                return None
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
                    result = linter.lint_file(str(md_file))  # type: ignore

                    if 'error' not in result:
                        fixes_applied = len(result.get('fixes', []))
                        size_reduction = result.get('size_reduction', 0)

                        total_fixes += fixes_applied
                        total_size_reduction += size_reduction
                        files_processed += 1

                        if fixes_applied > 0:
                            print(f"   ✅ {md_file.name}: {fixes_applied} fixes, {size_reduction} bytes saved")
                        else:
                            print(f"   ✅ {md_file.name}: Already clean")
                    else:
                        print(f"   ❌ {md_file.name}: {result['error']}")

            linting_stats = {
                'total_fixes': total_fixes,
                'total_size_reduction': total_size_reduction,
                'files_processed': files_processed,
                'avg_fixes_per_file': total_fixes / max(files_processed, 1),
                'avg_size_reduction': total_size_reduction / max(files_processed, 1)
            }

            print(f"✅ Linting complete: {total_fixes} total fixes, {total_size_reduction:,} bytes saved")
            return linting_stats

        except ImportError:
            print("⚠️  Linting module not available, skipping")
            return None
        except (RuntimeError, OSError, ValueError) as e:
            print(f"⚠️  Linting failed: {e}")
            return None

    def enhance_with_metadata(self, report, linting_stats):
        """Add metadata headers and session summaries to converted files"""
        if not report:
            print("⚠️  No report data available, skipping metadata enhancement")
            return

        self.print_step("7c", "Adding metadata to converted files")

        try:
            # Try to import metadata embedder dynamically
            import importlib.util
            utils_dir = Path(__file__).parent.parent / "utils"
            embedder_path = utils_dir / "metadata_embedder.py"

            enhance_function = None
            if embedder_path.exists():
                try:
                    spec = importlib.util.spec_from_file_location("metadata_embedder", embedder_path)
                    if spec and spec.loader:
                        embedder_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(embedder_module)
                        if hasattr(embedder_module, 'enhance_converted_files'):
                            enhance_function = getattr(embedder_module, 'enhance_converted_files')
                except (TypeError, AttributeError, ImportError, RuntimeError):
                    enhance_function = None

            if enhance_function and callable(enhance_function):
                # Prepare batch data for metadata enhancement
                batch_data = {
                    'session_id': self.session_id,
                    'batch_id': report.get('batch_id'),
                    'total_cost': report.get('actual_results', {}).get('total_cost', 0),
                    'total_files': report.get('actual_results', {}).get('total_requests', 0),
                    'total_pages': report.get('actual_results', {}).get('total_pages', 0),
                    'session_start': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Approximate
                    'session_end': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'files': []
                }

                # Add file details if available
                if 'file_details' in report:
                    for file_detail in report['file_details']:
                        batch_data['files'].append({
                            'name': file_detail.get('file', 'unknown.pdf'),
                            'pages': file_detail.get('pages', 0),
                            'cost': file_detail.get('cost', 0),
                            'cost_per_page': file_detail.get('cost_per_page', 0),
                            'tokens': file_detail.get('tokens', 0),
                            'final_size': file_detail.get('final_size', 'unknown')
                        })

                # Apply metadata enhancement
                try:
                    enhance_function(str(config.DEFAULT_CONVERTED_FOLDER), batch_data, linting_stats)
                    print("✅ Metadata enhancement completed")
                except (TypeError, AttributeError, RuntimeError) as e:
                    print(f"⚠️  Metadata enhancement failed: {e}")
            else:
                print("⚠️  Metadata enhancement function not found, skipping")

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
        actual_cost = usage_stats['total_cost']
        estimated_cost = estimates['estimated_cost']
        cost_diff = actual_cost - estimated_cost
        cost_diff_pct = (cost_diff / estimated_cost * 100) if estimated_cost > 0 else 0

        report = {
            'session_id': self.session_id,
            'batch_id': batch_id,
            'timestamp': datetime.now().isoformat(),
            'estimates': estimates,
            'actual_results': usage_stats,
            'comparison': {
                'cost_difference': cost_diff,
                'cost_difference_pct': cost_diff_pct,
                'pages_difference': usage_stats['total_requests'] - estimates['estimated_pages'],
                'tokens_difference': usage_stats['total_tokens'] - estimates['estimated_tokens']
            }
        }

        print(f"\n📊 COST ANALYSIS SUMMARY")
        print(f"{'='*50}")
        print(f"💰 Estimated Cost: ${estimated_cost:.4f}")
        print(f"💰 Actual Cost: ${actual_cost:.4f}")
        print(f"💰 Difference: ${cost_diff:+.4f} ({cost_diff_pct:+.1f}%)")
        print(f"📄 Pages Processed: {usage_stats['total_requests']}")
        print(f"🔢 Tokens Used: {usage_stats['total_tokens']:,}")
        print(f"⚡ Cost per Page: ${usage_stats['avg_cost_per_page']:.4f}")
        print(f"{'='*50}")

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
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
            print(f"   📊 Saved cost analysis: {report_file}")

        # Create summary file
        summary_file = session_folder / "README.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"# Batch Processing Session {self.session_id}\n\n")
            f.write(f"## Summary\n")
            f.write(f"- **Session ID:** {self.session_id}\n")
            f.write(f"- **Processed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            if report:
                f.write(f"- **Batch ID:** {report['batch_id']}\n")
                f.write(f"- **Files Processed:** {report['actual_results']['total_requests']}\n")
                f.write(f"- **Total Cost:** ${report['actual_results']['total_cost']:.4f}\n")
                f.write(f"- **Average Cost per Page:** ${report['actual_results']['avg_cost_per_page']:.4f}\n")
            f.write(f"\n## Contents\n")
            f.write(f"- `markdown_files/` - Converted markdown documents\n")
            f.write(f"- `cost_analysis.json` - Detailed cost breakdown\n")
            f.write(f"- `README.md` - This summary file\n")

        print(f"✅ Session organized: {session_folder}")
        return session_folder

    def cleanup_workspace(self):
        """Clean up temporary files"""
        print(f"\n🧹 Cleaning up workspace...")

        # Remove temp files but keep pdfs if they were copied
        cleanup_patterns = [
            "temp_batch",
            "batch_info_*.json",
            "usage_stats_*.json",
            str(config.DEFAULT_CONVERTED_FOLDER)
        ]

        cleaned = 0
        for pattern in cleanup_patterns:
            if "*" in pattern:
                for item in Path(".").glob(pattern):
                    try:
                        if item.is_dir():
                            shutil.rmtree(item)
                        else:
                            item.unlink()
                        cleaned += 1
                    except (OSError, PermissionError):
                        pass
            else:
                item = Path(pattern)
                if item.exists():
                    try:
                        if item.is_dir():
                            shutil.rmtree(item)
                        else:
                            item.unlink()
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

            # Step 9: Cleanup
            self.cleanup_workspace()

            # Final summary
            total_time = time.time() - start_time
            self.print_banner("PROCESSING COMPLETE! 🎉", "✅")
            print(f"⏱️  Total Time: {total_time/60:.1f} minutes")
            print(f"📁 Results: {final_folder}")
            if report:
                print(f"💰 Total Cost: ${report['actual_results']['total_cost']:.4f}")
                print(f"📄 Files Processed: {report['actual_results']['total_requests']}")
            print(f"✅ Ready to use!")

            return True

        except (RuntimeError, OSError, ValueError, KeyError) as e:
            self.print_banner("PROCESSING FAILED ❌", "❌")
            print(f"Error: {e}")
            print(f"Manual cleanup may be required.")
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
""")

    parser.add_argument('pdf_folder', nargs='?', default=str(config.DEFAULT_PDF_FOLDER),
                       help=f'Input folder containing PDF files (default: {config.DEFAULT_PDF_FOLDER})')
    parser.add_argument('output_folder', nargs='?', default=str(config.DEFAULT_CONVERTED_FOLDER),
                       help=f'Output folder for converted files (default: {config.DEFAULT_CONVERTED_FOLDER})')
    parser.add_argument('--no-lint', '--skip-lint', action='store_true',
                       help='Skip the markdown linting step (faster processing)')
    parser.add_argument('--no-metadata', action='store_true',
                       help='Skip metadata enhancement (embedded headers and summaries)')

    # Parse arguments
    args = parser.parse_args()

    # Show configuration
    print("🤖 Auto Batch PDF Converter")
    print(f"📁 Input Folder: {args.pdf_folder}")
    print(f"📁 Output Folder: {args.output_folder}")
    print(f"🔧 Linting: {'Disabled' if args.no_lint else 'Enabled'}")
    print(f"📊 Metadata: {'Disabled' if args.no_metadata else 'Enabled'}")
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
        enable_linting=not args.no_lint
    )
    success = processor.run_full_automation()

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
