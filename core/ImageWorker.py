import logging
import os

from .FileWorker import FileWorker

logger = logging.getLogger(__name__)


class ImageWorker(FileWorker):
    """
    Worker class for processing image files
    """

    def __init__(self, input_path: str):
        super().__init__(input_path)
        self.output_dir = os.path.dirname(input_path)
        logger.info("Processing image file %s", input_path)

    def convert_to_images(self) -> list[str]:
        """
        Mock function for image conversion

        Returns:
            List[str]: List of generated image paths
        """
        return [self.input_path]
