import argparse


class TerminalInterface:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(
            description='Sort images by visual similarity',
            epilog='Choose between SIFT and deep learning-based methods'
        )

        parser.add_argument(
            'method',
            choices=['sift', 'deeplearning'],
            help='Similarity detection method'
        )
        parser.add_argument(
            'source',
            type=str,
            help='Source folder containing images'
        )
        parser.add_argument(
            'destination',
            type=str,
            help='Destination folder for sorted images'
        )

        parser.add_argument(
            '-l', '--limit',
            type=int,
            help='Limit number of images to process'
        )
        parser.add_argument(
            '-v', '--verbose',
            action='store_true',
            help='Enable verbose logging'
        )
        parser.add_argument(
            '-t', '--threshold',
            type=float,
            default=0.7,
            help='Similarity threshold for grouping (default: 0.7)'
        )

        return parser.parse_args()