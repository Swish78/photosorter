import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
import numpy as np
from tqdm import tqdm
from .photo_handler import PhotoHandler


class ResNetProcessor:
    def __init__(self):
        # Set up device and model for feature extraction
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        weights = ResNet50_Weights.DEFAULT

        self.model = resnet50(weights=weights)
        self.model = nn.Sequential(*list(self.model.children())[:-1])

        for param in self.model.parameters():
            param.requires_grad = False

        self.model = self.model.to(self.device)
        self.transform = weights.transforms()

    def extract_features(self, image_paths):
        features = []

        for path in tqdm(image_paths, desc="Extracting ResNet Features"):
            image = PhotoHandler.prepare_image_for_torch(path)

            if image is None:
                features.append(np.zeros(2048))
                continue

            try:
                input_tensor = self.transform(image).unsqueeze(0).to(self.device)

                with torch.no_grad():
                    feature = self.model(input_tensor)
                    feature_vector = feature.squeeze().cpu().numpy().flatten()

                features.append(feature_vector)

            except Exception as e:
                print(f"ResNet feature extraction failed for {path}: {e}")
                features.append(np.zeros(2048))

        return np.array(features)