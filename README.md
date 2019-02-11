# Ai Data Preprocessing Queue

This tool is intended for preparing data for further processing.
It contains different text processing steps that can be enabled or disabled dynamically.

## Usage
```python
pipeline = Pipeline(['text_only', 'to_lower'])
value = pipeline.consume('Input text')
```
Note: Pipeline has to be instanciated only once and can be reused.

## Local installation

To install from master branch just use the following command:
```
pip install git+https://github.com/SamhammerAG/ai-data-preprocessing-queue.git@master#ai-data-preprocessing-queue
```
