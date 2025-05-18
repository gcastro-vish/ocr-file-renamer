from config import Settings

from typing import Optional
from pathlib import Path
import cv2
import os


class Image:
    def __init__(self, path: str) -> None:
        p = Path(path)
        name = p.parts[-1]
        self.name = name
        self.original_image = cv2.imread(path)
        self.actual_image = cv2.imread(path)
        self.h, self.w, _ = self.actual_image.shape

    def crop_image(self, hs: float=0.5, ws: float=0.5) -> None:
        new_h = self.h*hs
        new_w = self.w*ws
        try: 
            self.actual_image = self.actual_image[int(new_h):, int(new_w):]
            self.h = new_h
            self.w = new_w
        except Exception as e:
            print(f"Erro ao 'cropar' a imagem: {e}")
            self.dump_image("failed")
    
    def scale_color_image(self, color_scale: int=cv2.COLOR_BGR2GRAY) -> None:
        try: 
            self.actual_image = cv2.cvtColor(self.actual_image, color_scale)
        except Exception as e:
            print(f"Erro ao cropar a imagem: {e}")
            self.dump_image("failed")
    
    def dump_image(self, objective: str, name: Optional[str]=None) -> None:
        name = self.name if name is None else name
        match objective:
            case "backup":
                cv2.imwrite(str(Settings.BACKUP_FOLDER / name), self.original_image)
            
            case "debug":
                cv2.imwrite(str(Settings.DEBUG_FOLDER / name), self.original_image)
            
            case "failed":
                cv2.imwrite(str(Settings.FAILED_FOLDER / name), self.original_image)
            
            case "processed":
                cv2.imwrite(str(Settings.PROCESSED_FOLDER / name), self.original_image)

            case "partial":
                cv2.imwrite(str(Settings.PARTIAL_FOLDER / name), self.original_image)

    def process_image(self) -> None:
        self.crop_image(hs=0.5, ws=0.5)
        self.scale_color_image(color_scale=cv2.COLOR_BGR2GRAY)

    def get_image(self) -> cv2.typing.MatLike:
        return self.actual_image
    
    def get_image_name(self) -> str:
        return self.name
    
    def move_to_backup(self, img_path: str) -> None:
        self.dump_image("backup")
        os.remove(img_path)