#!/usr/bin/env python3
"""
Enhanced Auto Batch PDF Converter with Embedded Metadata
Adds conversion metadata to each file and creates session summaries
"""

import os
from datetime import datetime
from pathlib import Path


class MetadataEmbedder:
    """Handles embedding conversion metadata into markdown files"""

    def __init__(self):
        self.session_start = None
        self.session_end = None
        self.total_cost = 0
        self.total_files = 0
        self.total_pages = 0
        self.files_data = []
        self.batch_id = None
        self.linting_stats = None
        self.session_id = None

    def add_file_metadata(self, md_file_path, file_data):
        """Add conversion metadata header to a markdown file"""
        if not os.path.exists(md_file_path):
            return False

        # Read the original content
        with open(md_file_path, encoding="utf-8") as f:
            original_content = f.read()

        # Extract file info
        filename = os.path.basename(md_file_path)
        file_info = file_data.get(filename.replace("_batch.md", ""), {})

        # Create metadata header
        metadata_header = self._create_file_header(filename, file_info)

        # Combine header with content
        enhanced_content = metadata_header + "\n" + original_content

        # Write back to file
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(enhanced_content)

        return True

    def _create_file_header(self, filename, file_info):
        """Create the metadata header for individual files"""
        header = "<!--\n"
        header += "=" * 60 + "\n"
        header += "MARKPDFDOWN CONVERSION METADATA\n"
        header += "=" * 60 + "\n"
        header += f"File: {filename}\n"
        header += f"Converted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        header += f"Source PDF: {file_info.get('source_pdf', 'Unknown')}\n"
        header += f"Batch ID: {self.batch_id or 'Unknown'}\n"
        header += f"Session ID: {getattr(self, 'session_id', 'Unknown')}\n"
        header += "-" * 60 + "\n"
        header += "PROCESSING DETAILS:\n"
        header += f"Pages Processed: {file_info.get('pages', 'Unknown')}\n"
        header += f"API Cost: ${file_info.get('cost', 0):.4f}\n"
        header += f"Cost per Page: ${file_info.get('cost_per_page', 0):.4f}\n"
        tokens = file_info.get("tokens", "Unknown")
        if isinstance(tokens, (int, float)):
            header += f"Tokens Used: {tokens:,}\n"
        else:
            header += f"Tokens Used: {tokens}\n"
        if self.linting_stats:
            header += f"Post-Processing: Linted ({self.linting_stats.get('fixes', 0)} fixes applied)\n"
            if "size_reduction" in self.linting_stats:
                header += f"Size Optimization: {self.linting_stats['size_reduction']:,} bytes saved\n"
        header += "-" * 60 + "\n"
        header += "BATCH CONTEXT:\n"
        header += f"Total Files in Batch: {self.total_files}\n"
        header += f"Total Batch Cost: ${self.total_cost:.4f}\n"
        header += f"Average Batch Cost/Page: ${(self.total_cost / max(self.total_pages, 1)):.4f}\n"
        if self.session_start and self.session_end:
            try:
                if isinstance(self.session_start, str):
                    start_time = datetime.strptime(
                        self.session_start, "%Y-%m-%d %H:%M:%S"
                    )
                else:
                    start_time = self.session_start

                if isinstance(self.session_end, str):
                    end_time = datetime.strptime(self.session_end, "%Y-%m-%d %H:%M:%S")
                else:
                    end_time = self.session_end

                processing_time = (end_time - start_time).total_seconds() / 60
                header += f"Processing Time: {processing_time:.1f} minutes\n"
            except (ValueError, TypeError):
                # Skip processing time if we can't parse the dates
                pass
        header += "=" * 60 + "\n"
        header += "-->\n"
        return header

    def create_session_summary(self, output_dir, batch_data):
        """Create a comprehensive session summary markdown file"""
        session_file = (
            Path(output_dir)
            / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_conversion_summary.md"
        )

        with open(session_file, "w", encoding="utf-8") as f:
            f.write(self._generate_session_summary_content(batch_data))

        return session_file

    def _generate_session_summary_content(self, _batch_data):
        """Generate the content for session summary"""
        content = (
            f"# Conversion Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        # Session Overview
        content += "## 📊 Session Overview\n\n"
        content += f"- **Date**: {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}\n"
        content += f"- **Session ID**: {getattr(self, 'session_id', 'Unknown')}\n"
        content += f"- **Batch ID**: {self.batch_id or 'Unknown'}\n"
        content += f"- **Total Files**: {self.total_files}\n"
        content += f"- **Total Pages**: {self.total_pages}\n"
        content += f"- **Total Cost**: ${self.total_cost:.4f}\n"

        if self.session_start and self.session_end:
            try:
                if isinstance(self.session_start, str):
                    start_time = datetime.strptime(
                        self.session_start, "%Y-%m-%d %H:%M:%S"
                    )
                else:
                    start_time = self.session_start

                if isinstance(self.session_end, str):
                    end_time = datetime.strptime(self.session_end, "%Y-%m-%d %H:%M:%S")
                else:
                    end_time = self.session_end

                processing_time = (end_time - start_time).total_seconds() / 60
                content += f"- **Processing Time**: {processing_time:.1f} minutes\n"
            except (ValueError, TypeError):
                # Skip processing time if we can't parse the dates
                pass

        content += f"- **Average Cost/Page**: ${(self.total_cost / max(self.total_pages, 1)):.4f}\n\n"

        # Cost Analysis
        content += "## 💰 Cost Analysis\n\n"
        content += "- **API Method**: OpenAI Batch API (50% savings)\n"
        content += f"- **Total API Cost**: ${self.total_cost:.4f}\n"
        content += "- **Linting Cost**: $0.00 (local processing)\n"
        content += f"- **Cost Efficiency**: ${(self.total_cost / max(self.total_pages, 1)):.4f} per page\n\n"

        # Files Processed Table
        content += "## 📄 Files Processed\n\n"
        content += "| File | Pages | Cost | Cost/Page | Tokens | Final Size |\n"
        content += "|------|-------|------|-----------|--------|-----------|\n"

        for file_data in self.files_data:
            name = file_data.get("name", "Unknown")[:40] + (
                "..." if len(file_data.get("name", "")) > 40 else ""
            )
            pages = file_data.get("pages", 0)
            cost = file_data.get("cost", 0)
            cost_per_page = file_data.get("cost_per_page", 0)
            tokens = file_data.get("tokens", 0)
            size = file_data.get("final_size", "Unknown")

            content += f"| {name} | {pages} | ${cost:.4f} | ${cost_per_page:.4f} | {tokens:,} | {size} |\n"

        content += "\n"

        # Post-Processing Stats
        if self.linting_stats:
            content += "## 🔧 Post-Processing Results\n\n"
            content += "- **Linting Applied**: Yes\n"
            content += f"- **Total Fixes Applied**: {self.linting_stats.get('total_fixes', 0)}\n"
            content += f"- **Size Reduction**: {self.linting_stats.get('total_size_reduction', 0):,} bytes\n"
            if self.linting_stats.get("files_processed", 0) > 0:
                avg_reduction = self.linting_stats.get(
                    "total_size_reduction", 0
                ) / self.linting_stats.get("files_processed", 1)
                content += (
                    f"- **Average Reduction per File**: {avg_reduction:,.0f} bytes\n"
                )
            content += "- **Optimization Cost**: $0.00 (local processing)\n\n"

        # Comparative Analysis Section
        content += "## 📈 Session Comparison Template\n\n"
        content += "Use this section to compare with other conversion sessions:\n\n"
        content += "| Metric | This Session | Previous Session | Comparison |\n"
        content += "|--------|-------------|------------------|------------|\n"
        content += f"| Files | {self.total_files} | _[Enter Previous]_ | _[+/- Difference]_ |\n"
        content += f"| Pages | {self.total_pages} | _[Enter Previous]_ | _[+/- Difference]_ |\n"
        content += f"| Cost | ${self.total_cost:.4f} | _[Enter Previous]_ | _[+/- Difference]_ |\n"
        content += f"| Cost/Page | ${(self.total_cost / max(self.total_pages, 1)):.4f} | _[Enter Previous]_ | _[+/- Difference]_ |\n"
        if self.session_start and self.session_end:
            try:
                if isinstance(self.session_start, str):
                    start_time = datetime.strptime(
                        self.session_start, "%Y-%m-%d %H:%M:%S"
                    )
                else:
                    start_time = self.session_start

                if isinstance(self.session_end, str):
                    end_time = datetime.strptime(self.session_end, "%Y-%m-%d %H:%M:%S")
                else:
                    end_time = self.session_end

                processing_time = (end_time - start_time).total_seconds() / 60
                content += f"| Time (min) | {processing_time:.1f} | _[Enter Previous]_ | _[+/- Difference]_ |\n"
            except (ValueError, TypeError):
                # Skip processing time if we can't parse the dates
                pass
        content += "\n"

        # Usage Notes
        content += "## 📝 Usage Notes\n\n"
        content += "- Each converted markdown file contains embedded metadata in HTML comments\n"
        content += "- Metadata includes individual file costs, processing details, and batch context\n"
        content += "- This summary provides session-level analytics for comparison across batches\n"
        content += "- Cost analysis uses OpenAI Batch API pricing (50% savings vs standard API)\n"
        content += (
            "- Local linting provides additional optimization at zero API cost\n\n"
        )

        content += "---\n"
        content += f"*Generated by MarkPDFDown Auto Batch Processor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

        return content


def enhance_converted_files(converted_dir, batch_data, linting_stats=None):
    """Main function to add metadata to all converted files and create summary"""
    embedder = MetadataEmbedder()

    # Set session data
    embedder.session_id = batch_data.get(
        "session_id", datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    embedder.batch_id = batch_data.get("batch_id")
    embedder.total_cost = batch_data.get("total_cost", 0)
    embedder.total_files = batch_data.get("total_files", 0)
    embedder.total_pages = batch_data.get("total_pages", 0)
    embedder.files_data = batch_data.get("files", [])
    embedder.session_start = batch_data.get("session_start")
    embedder.session_end = batch_data.get("session_end")
    embedder.linting_stats = linting_stats

    # Add metadata to each file
    converted_path = Path(converted_dir)
    if converted_path.exists():
        for md_file in converted_path.glob("*.md"):
            if not md_file.name.endswith("_summary.md"):  # Skip existing summaries
                file_info = {}
                # Find matching file data
                for file_data in embedder.files_data:
                    if file_data.get("name", "").replace(".pdf", "") in md_file.name:
                        file_info = file_data
                        break

                embedder.add_file_metadata(str(md_file), {"filename": file_info})
                print(f"   📝 Added metadata to {md_file.name}")

    # Create session summary
    summary_file = embedder.create_session_summary(converted_dir, batch_data)
    print(f"   📊 Created session summary: {summary_file.name}")

    return summary_file


if __name__ == "__main__":
    # Test the metadata embedder
    print("🔧 Testing Metadata Embedder...")

    # Example usage
    test_data = {
        "session_id": "20250716_123456",
        "batch_id": "batch_test123",
        "total_cost": 1.50,
        "total_files": 3,
        "total_pages": 45,
        "session_start": datetime.now(),
        "session_end": datetime.now(),
        "files": [
            {
                "name": "doc1.pdf",
                "pages": 15,
                "cost": 0.75,
                "cost_per_page": 0.05,
                "tokens": 1000,
            },
            {
                "name": "doc2.pdf",
                "pages": 20,
                "cost": 0.50,
                "cost_per_page": 0.025,
                "tokens": 1500,
            },
            {
                "name": "doc3.pdf",
                "pages": 10,
                "cost": 0.25,
                "cost_per_page": 0.025,
                "tokens": 800,
            },
        ],
    }

    linting_data = {
        "total_fixes": 15,
        "total_size_reduction": 50000,
        "files_processed": 3,
    }

    print("✅ Test data prepared")
