import logging
import os

logger = logging.getLogger(__name__)


class FileWorker:
    """
    Base class Worker, define common interface
    """

    def __init__(self, input_path: str):
        """
        Initialize Worker

        Args:
            input_path (str): Input file path
        """
        self.input_path = input_path

    def convert_to_images(self, output_dir: str = ".", **kwargs) -> list[str]:
        """
        Convert input file to images

        Args:
            output_dir (str): Output directory
            **kwargs: Other parameters

        Returns:
            List[str]: List of generated image paths
        """
        raise NotImplementedError("Subclasses must implement this method")


def create_worker(input_path: str, start_page: int = 1, end_page: int = 0):
    """
    Create corresponding Worker instance based on file extension

    Args:
        input_path (str): Input file path
        start_page (int): Starting page number
        end_page (int): Ending page number

    Returns:
        Worker: Worker instance
    """
    _, ext = os.path.splitext(input_path)
    ext = ext.lower()

    worker = None
    if ext == ".pdf":
        from .PDFWorker import PDFWorker

        worker = PDFWorker(input_path, start_page, end_page)
    elif ext == ".jpg" or ext == ".jpeg" or ext == ".png" or ext == ".bmp":
        from .ImageWorker import ImageWorker

        worker = ImageWorker(input_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return worker
