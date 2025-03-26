import os
import cv2
from PIL import Image


class PhotoHandler:
    @staticmethod
    def get_image_paths(source_folder, limit=None, extensions=None):
        if extensions is None:
            extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}

        image_paths = [
            os.path.join(source_folder, f)
            for f in os.listdir(source_folder)
            if os.path.splitext(f)[1].lower() in extensions
        ]

        return image_paths[:limit] if limit else image_paths

    @staticmethod
    def prepare_image_for_cv2(image_path):
        try:
            return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            return None

    @staticmethod
    def prepare_image_for_torch(image_path):
        try:
            return Image.open(image_path).convert('RGB')
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            return None

    @staticmethod
    def create_output_directory(destination_folder):
        os.makedirs(destination_folder, exist_ok=True)