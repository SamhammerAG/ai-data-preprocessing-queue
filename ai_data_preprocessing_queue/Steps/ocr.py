import numpy as np
import pytesseract
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from langdetect import detect, detect_langs
from pdfplumber import page
from cv2 import cv2


langMapping = {
    'deu': 'de',
    'eng': 'en',
    'rus': 'ru',
    'spa': 'sp'
}


def step(item, itemState, globalState, preprocessorData: str):

    text = ''

    if type(item) == np.ndarray or type(item) == JpegImageFile:
        if globalState and globalState.get('image_to_string', {}).get("lang"):
            params = globalState.get('image_to_string')
        else:
            params = {"lang": "deu", "config": "--psm 1"}

        _text = str((pytesseract.image_to_string(item, **params)))
        best_prob = 0

        for i in range(0, 4):
            langs = detect_langs(_text[:100])
            language = langs[0].lang
            prob = langs[0].prob

            if language == langMapping.get(params.get("lang")):
                text = _text
                break

            if prob > best_prob:
                best_prob = prob
                text = _text

            if type(item) == np.ndarray:
                item = cv2.rotate(item, cv2.ROTATE_90_CLOCKWISE)
            if type(item) == JpegImageFile:
                item.transpose(Image.ROTATE_90)
            _text = str((pytesseract.image_to_string(item, lang=params.get('lang'), config='--psm 6')))

    elif type(item) == page.Page:
        text = item.extract_text()

    return text


