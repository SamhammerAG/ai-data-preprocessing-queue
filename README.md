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

## Existing preprocessors

### Number Interpretation Preprocessor
This one will take your text and search for occurences of specific entities. Those are replaced by keywords. Using this approach, two text corpa are similar if both contain IBAN/Phonenumbers/etc.

**How it works**
The number_interpretation.py reads all files within number_interpretation_preprocessor, instantiates the classes and runs the text through all replacer.

**How to add new replacer**
- Add a new one that inherits from `BaseReplacer` and implement the methods
- add an import to the `__init__.py`
- add an unit test to `tests.py`
