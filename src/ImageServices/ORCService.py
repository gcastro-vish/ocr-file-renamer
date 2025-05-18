from .ImageService import Image
from config import Settings

from typing import Optional
import pytesseract
import re

if Settings.TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = Settings.TESSERACT_PATH


class ORCHandler:
    @classmethod
    def get_text(cls, img: Image) -> str:
        try:
            return pytesseract.image_to_string(img.get_image())
        except pytesseract.pytesseract.TesseractNotFoundError:
            print("Tesseract não encontrado. Por favor instale-o ou corriga o caminho no arquivo '.env'.")
            return ""
    
    @classmethod
    def get_date(cls, text: str) -> Optional[str]:
        date_pattern = r'\d{1,2}\s+de\s+\w{3,}\.?\s+de\s+\d{4}'   
        date_match = re.search(date_pattern, text)
    
        return date_match.group(0) if date_match else None
    
    @classmethod
    def get_time(cls, text: str) -> Optional[str]:
        time_pattern = r'\b\d{2}:\d{2}:\d{2}\b'
        time_match = re.search(time_pattern, text)
        
        return time_match.group(0) if time_match else None