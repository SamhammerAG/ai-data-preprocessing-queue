# Ai Data Preprocessing Queue

This tool is intended for preparing data for further processing.
It contains different text processing steps that can be enabled or disabled dynamically.

## Usage
```python
from ai_data_preprocessing_queue import Pipeline

state = {}
pre_processor_dict = {
  'to_lower' : None,
  'spellcheck' : 'test\r\ntesting'
}
pipeline = Pipeline(pre_processor_dict)
value = pipeline.consume('Input text', state)
```
        

State is optional here and can be used to cache preprocessing data between pipeline calls.

The preprocessors that the pipeline should use have to be transmitted as keys within a dictionary.  
Some preprocessors also require additional data to function.  
The data has to be converted to a string-form and assigned to it's preprocessor within the dictionary.

This dictionary then needs to be transmitted to the pipeline through it's constructor.

```python
import pdfplumber
from ai_data_preprocessing_queue import Pipeline

state = {"image_to_string": {"lang": "deu", "config": "--psm 1"}}
pipeline = Pipeline({'ocr': None, 'text_only': None})

value = ""
with pdfplumber.open('test.pdf') as pdf:
    for page in pdf.pages:
        value += pipeline.consume(page, state)

```

Ocr step should be used first in the pipeline.

For more info about which preprocessors need data and how this data needs to be formatted, see the preprocessor list below.

Note: Pipeline has to be instantiated only once and can be reused.

## Local installation

To install from master branch just use the following command:
```
pip install git+https://github.com/SamhammerAG/ai-data-preprocessing-queue.git@master#ai-data-preprocessing-queue
```
Install Tesseract Application with required languages (see OCR article in confluence), and add location to the PATH Environment Variable (Path=C:\...). 

## Existing preprocessors

### OCR
Name: to_lower  
Required additional data: -  
Converts the text to lower case characters. This step accepts a `np.ndarray` from `PIL.Image.open`, `PIL.JpegImagePlugin.JpegImageFile` or `pdfplumber.page.Page` as `item` parameter.

### To Lower Case
Name: ocr  
Required additional data: -  
Converts jpg, tiff files or pdf pages into a text. 


### Remove Numbers
Name: remove_numbers  
Required additional data: -  
Removes all numbers from the text.

### Remove Punctuation
Name: remove_punctuation  
Required additional data: -  
Removes all special characters from the text.

### Text only
Name: text_only  
Required additional data: -  
Removes all special characters and numbers from the text.

### Spellcheck (Levenshtein)
Name: spellcheck  
Required additional data: A string containing words, separated by newline, i.e. "word1\r\nword2"  
Takes a list of words which depict correct spelling. Words within the given text that are close to a word from this list will be replaced with the listed word.

### Regex replacement
Name: regex_replacement  
Required additional data: CSV-Data in string form with following line-format: &lt;pattern&gt;,&lt;replacement&gt;,&lt;order&gt;
  - pattern: a regex pattern that is to be found within the text
  - replacement: the word/text, with which any match should be replaced
  - order: the order of the entries, in which they should be applied (lowest number will be applied first!)

This one will take your text and search for occurences of specific entities. Those are replaced by keywords. Using this approach, two text corpa are similar if both contain IBAN/Phonenumbers/etc.

### Token Replacement
Name: token_replacement  
Required additional data: CSV-Data in string form with following line-format: &lt;text&gt;,&lt;replacement&gt;,&lt;order&gt;
  - text: one or multiple words to search within the text
  - replacement: the word/text, with which any match should be replaced
  - order: the order of the entries, in which they should be applied (largest number will be applied first!)

With this preprocessor you can replace specific words and abbreviations within the text with specified tokens.
It is also possible to replace abbreviations that are ending with a dot. Other special characters are not supported, though.
