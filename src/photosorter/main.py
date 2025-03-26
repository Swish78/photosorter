import os
import shutil
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .terminal_interface import TerminalInterface
from .photo_handler import PhotoHandler
from .sift_processor import SIFTProcessor
from .resnet_processor import ResNetProcessor


class ImageSimilaritySorter:
    def __init__(self, method='encoder', verbose=False, threshold=0.7):
        self.method = method
        self.verbose = verbose
        self.threshold = threshold

        self.processor = (
            SIFTProcessor() if method == 'sift'
            else ResNetProcessor()
        )

    def sort_images(self, source_folder, destination_folder, limit=None):
        PhotoHandler.create_output_directory(destination_folder)

        image_paths = PhotoHandler.get_image_paths(source_folder, limit)

        if not image_paths:
            print("No images found in the source folder.")
            return

        feature_vectors = self.processor.extract_features(image_paths)

        similarity_matrix = cosine_similarity(feature_vectors)

        self._group_and_copy_images(
            image_paths,
            similarity_matrix,
            destination_folder
        )

    def _group_and_copy_images(self, image_paths, similarity_matrix, destination):
        processed = set()
        group_count = 1

        for i in range(len(image_paths)):
            if i in processed:
                continue

            group_folder = os.path.join(destination, f'similarity_group_{group_count}')
            os.makedirs(group_folder, exist_ok=True)

            ref_image_path = image_paths[i]
            ref_filename = os.path.basename(ref_image_path)
            shutil.copy2(ref_image_path, os.path.join(group_folder, ref_filename))

            processed.add(i)

            for j in range(i + 1, len(image_paths)):
                if j in processed:
                    continue

                if similarity_matrix[i][j] >= self.threshold:
                    similar_image_path = image_paths[j]
                    similar_filename = os.path.basename(similar_image_path)
                    shutil.copy2(similar_image_path, os.path.join(group_folder, similar_filename))
                    processed.add(j)

            group_count += 1


def main():
    args = TerminalInterface.parse_arguments()
    sorter = ImageSimilaritySorter(
        method=args.method,
        verbose=args.verbose,
        threshold=args.threshold
    )
    sorter.sort_images(
        args.source,
        args.destination,
        args.limit
    )


if __name__ == "__main__":
    main()