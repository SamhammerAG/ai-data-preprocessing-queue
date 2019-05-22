#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ai-data-preprocessing-queue",
    version="1.0.0",
    description="Can be used to pre process data before ai processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamhammerAG/ai-data-preprocessing-queue",
    packages=find_packages(exclude=["test_data"]),
    install_requires=['langdetect==1.0.7', 'nltk==3.4', "pandas==0.24.2", "numpy==1.16"]
)
