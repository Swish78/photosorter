# PhotoSorter

Automatically group similar images using computer vision techniques.

## Installation

```bash
pip install photosorter
```

## Usage

After installation, you can use the `photosorter` command directly from your terminal:

```bash
photosorter [sift|deeplearning] SOURCE DESTINATION [-t THRESHOLD] [-l LIMIT] [-v]
```

### Arguments
- `method`: Similarity detection method (sift/deeplearning)
- `source`: Source directory containing images
- `destination`: Output directory for grouped images

### Options
- `-t, --threshold`: Similarity threshold (0.0-1.0)
- `-l, --limit`: Maximum number of images to process
- `-v, --verbose`: Enable detailed processing output

## Methods
1. **SIFT** - Traditional feature matching using Scale-Invariant Feature Transform
2. **DeepLearning** - ResNet-50 embeddings with cosine similarity comparison

## Example
```bash
# Using deep learning method with 0.8 similarity threshold
photosorter deeplearning ./photos ./sorted_images -t 0.8
```
