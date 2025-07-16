import logging
import os

import PyPDF2

from .FileWorker import FileWorker

logger = logging.getLogger(__name__)


class PDFWorker(FileWorker):
    """
    Worker class for processing PDF files
    """

    def __init__(self, input_path: str, start_page: int = 1, end_page: int = 0):
        super().__init__(input_path)
        self.reader = PyPDF2.PdfReader(input_path)
        self.total_pages = len(self.reader.pages)
        self.start_page = start_page
        self.end_page = end_page
        self.output_dir = os.path.dirname(input_path)

        # First validate page number range
        if start_page < 1 or start_page > self.total_pages:
            start_page = 1
        if end_page == 0 or end_page > self.total_pages:
            end_page = self.total_pages

        logger.info("Processing PDF from page %d to page %d", start_page, end_page)

        # If page number range is the entire document, no extraction is needed
        if start_page == 1 and end_page == self.total_pages:
            return

        # Extract specified page number range of PDF
        extracted_path = self.extract_pages(start_page, end_page)
        if not extracted_path:
            logger.warning("Page extraction failed, using original file")
            return

        logger.info("Page extraction completed")
        self.input_path = extracted_path

    def get_total_pages(self) -> int:
        """
        Get the total number of pages in the PDF

        Returns:
            int: Total number of pages
        """
        return self.total_pages

    def extract_pages(
        self, start_page: int, end_page: int, output_name: str = None
    ) -> str:
        """
        Extract PDF content from a specified page range

        Args:
            start_page (int): Starting page number (starts from 1)
            end_page (int): Ending page number (starts from 1)
            output_name (str): Custom output file name (optional)

        Returns:
            str: Generated PDF file path, empty string on failure
        """
        try:
            # Convert page numbers to 0-based index
            start = max(0, start_page - 1)
            end = min(self.total_pages - 1, end_page - 1)

            if start > end:
                start, end = end, start  # Automatically correct page number order

            writer = PyPDF2.PdfWriter()

            # Add content from specified pages
            for page_num in range(start, end + 1):
                writer.add_page(self.reader.pages[page_num])

            # Generate output file name
            if not output_name:
                base_name = os.path.basename(self.input_path).rsplit(".", 1)[0]
                output_name = f"{base_name}_pages_{start_page}-{end_page}.pdf"

            os.makedirs(self.output_dir, exist_ok=True)
            output_path = os.path.join(self.output_dir, output_name)

            # Write to file
            with open(output_path, "wb") as out_file:
                writer.write(out_file)

            return output_path

        except Exception as e:
            logger.error(f"Page extraction failed: {str(e)}")
            return ""

    def convert_to_images(self, dpi: int = 300, fmt: str = "jpg") -> list[str]:
        """
        Convert each PDF page to a high-quality image

        Args:
            dpi (int): Output image resolution (default 300)
            fmt (str): Image format (supports jpg/png, default jpg)

        Returns:
            List[str]: List of generated image paths
        """
        try:
            import fitz  # PyMuPDF

            os.makedirs(self.output_dir, exist_ok=True)
            img_paths = []

            doc = fitz.open(self.input_path)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap(dpi=dpi)
                output_path = os.path.join(
                    self.output_dir, f"page_{page_num + 1:04d}.{fmt}"
                )
                pix.save(output_path)
                img_paths.append(output_path)

            return img_paths

        except Exception as e:
            logger.error(f"PDF conversion to images failed: {str(e)}")
            return []
