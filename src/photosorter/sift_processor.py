import numpy as np
import cv2
from tqdm import tqdm
from .photo_handler import PhotoHandler


class SIFTProcessor:
    def __init__(self):
        self.sift = cv2.SIFT_create()

    def extract_features(self, image_paths):
        features = []

        for path in tqdm(image_paths, desc="Extracting SIFT Features"):
            img = PhotoHandler.prepare_image_for_cv2(path)

            if img is None:
                features.append(np.zeros(128))
                continue

            try:
                kp, des = self.sift.detectAndCompute(img, None)

                feature_vector = des.mean(axis=0) if des is not None else np.zeros(128)
                features.append(feature_vector)

            except Exception as e:
                print(f"SIFT feature extraction failed for {path}: {e}")
                features.append(np.zeros(128))

        return np.array(features)