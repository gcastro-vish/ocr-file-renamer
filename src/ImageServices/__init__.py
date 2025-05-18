from .ORCService import ORCHandler
from .ImageService import Image

ocr_handler = ORCHandler()

__all__ = ["Image", "ocr_handler"]