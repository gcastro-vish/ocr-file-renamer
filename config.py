from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    NEW_FOLDER=Path(__name__).resolve().parent / "data" / "new"
    BACKUP_FOLDER=Path(__name__).resolve().parent / "data" / "backup"
    PROCESSED_FOLDER=Path(__name__).resolve().parent / "data" / "processed"
    DEBUG_FOLDER=Path(__name__).resolve().parent / "data" / "debug"
    FAILED_FOLDER=Path(__name__).resolve().parent / "data" / "failed"
    PARTIAL_FOLDER=Path(__name__).resolve().parent / "data" / "partial"
    
    TESSERACT_PATH=os.getenv("TESSERACT_PATH")

os.makedirs(Settings.NEW_FOLDER, exist_ok=True)
os.makedirs(Settings.BACKUP_FOLDER, exist_ok=True)
os.makedirs(Settings.PROCESSED_FOLDER, exist_ok=True)
os.makedirs(Settings.DEBUG_FOLDER, exist_ok=True)
os.makedirs(Settings.FAILED_FOLDER, exist_ok=True)
os.makedirs(Settings.PARTIAL_FOLDER, exist_ok=True)