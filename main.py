import os
from tqdm import tqdm

from config import Settings
from src.ImageServices import *
from src.DateServices import *


def main():
    img_list = os.listdir(Settings.NEW_FOLDER)

    for img_name in tqdm(img_list, desc="Processing Images"):
        try:
            img_path = Settings.NEW_FOLDER / img_name
            
            img = Image(path = img_path)
            
            img.move_to_backup(img_path)
            
            img.process_image()
            
            text = ocr_handler.get_text(img)
            
            raw_date = ocr_handler.get_date(text)
            time = ocr_handler.get_time(text)

            if raw_date is None and time is None:
                img.dump_image("failed")
                continue
            
            if raw_date is not None:
                processed_date = normalizer.normalize(raw_date)
            else:
                img.dump_image("partial", f"{time}__{img.get_image_name()}")
                continue

            if processed_date and time:
                new_file_name = f"{processed_date}__{time}.jpeg"
                objective = "processed"
            else:
                base = processed_date or raw_date or time
                new_file_name = f"{base}__{img.get_image_name()}"
                objective = "partial"
            
            img.dump_image(objective, name=new_file_name)

        except Exception as e:
            raise e
            print(f"Unexpected error processing {img_name}: {e}")
            img.dump_image("failed")
            continue

if __name__ == "__main__":
    print("Starting")
    main()
    print("Stoping")