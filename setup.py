from setuptools import setup, find_packages

setup(
    name="photosorter",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[
        "numpy>=1.19.0",
        "scikit-learn>=0.24.0",
        "opencv-python>=4.5.0",
        "torchvision>=0.8.0",
        "torch>=1.7.0",
        "pillow>=8.0.0",
        "tqdm>=4.50.0"
    ],
    entry_points={
        "console_scripts": [
            "photosorter=photosorter.main:main"
        ]
    },
    author="Swayam Patil",
    description="Automatically group similar images using computer vision techniques",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Swish78/photosorter",
    keywords="computer-vision, image-processing, similarity-detection",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
}
