#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ai-data-preprocessing-queue",
    version="1.2.1",
    description="Can be used to pre process data before ai processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamhammerAG/ai-data-preprocessing-queue",
    packages=find_packages(exclude=["test_data"]),
    install_requires=["langdetect==1.0.8", "nltk~=3.6.6", "pandas==1.0.3", "numpy~=1.23.4", "pytesseract == 0.3.9",
                      "pdfplumber== 0.6.0", "opencv-python==4.5.5.64", "Pillow==9.0.1"]
)