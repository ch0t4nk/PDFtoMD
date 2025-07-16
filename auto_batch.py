#!/usr/bin/env python3
"""
Auto Batch PDF Converter - Fully Automated PDF to Markdown Conversion
Usage: python auto_batch.py [pdf_folder] [output_folder]
"""

import os
import sys
import time
import json
import shutil
from pathlib import Path
from datetime import datetime
from master import PDFBatchMaster
from batch_api import BatchPDFConverter

class AutoBatchProcessor:
    def __init__(self, pdf_folder="pdfs", output_folder="converted_markdown"):
        self.pdf_folder = Path(pdf_folder)
        self.output_folder = Path(output_folder)
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
        temp_pdfs = Path("pdfs")
        if not temp_pdfs.exists() or temp_pdfs != self.pdf_folder:
            temp_pdfs.mkdir(exist_ok=True)
            
            # Copy PDFs to workspace
            print(f"📂 Copying PDFs to workspace...")
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
        pdf_dir = Path("pdfs")
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
    
    def analyze_costs(self, batch_id, estimates):
        """Analyze final costs and compare to estimates"""
        self.print_step(7, "Analyzing costs and generating report")
        
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
        converted_dir = Path("converted")
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
            "converted"
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
                    except Exception:
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
                    except Exception:
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
                raise Exception("Batch processing failed")
            
            # Step 6: Retrieve results
            if not self.retrieve_results(batch_id):
                raise Exception("Failed to retrieve results")
            
            # Step 7: Analyze costs
            report = self.analyze_costs(batch_id, estimates)
            
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
            
        except Exception as e:
            self.print_banner("PROCESSING FAILED ❌", "❌")
            print(f"Error: {e}")
            print(f"Manual cleanup may be required.")
            return False

def main():
    """Main entry point"""
    if len(sys.argv) == 1:
        print("🤖 Auto Batch PDF Converter")
        print("\nUsage:")
        print("  python auto_batch.py                     # Use default folders (pdfs -> converted_markdown)")
        print("  python auto_batch.py <pdf_folder>        # Specify input folder")
        print("  python auto_batch.py <pdf_folder> <output_folder>  # Specify both folders")
        print("\nThis script will:")
        print("  1. 🔍 Scan for PDFs in the input folder")
        print("  2. 📊 Estimate processing costs")
        print("  3. 🚀 Submit batch to OpenAI")
        print("  4. ⏰ Monitor progress automatically")
        print("  5. 📥 Retrieve results when complete")
        print("  6. 💰 Generate cost analysis")
        print("  7. 📁 Organize outputs in timestamped session folder")
        print("  8. 🧹 Clean up temporary files")
        return
    
    # Parse arguments
    pdf_folder = sys.argv[1] if len(sys.argv) > 1 else "pdfs"
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "converted_markdown"
    
    # Run automation
    processor = AutoBatchProcessor(pdf_folder, output_folder)
    success = processor.run_full_automation()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
