from typing import Any, Dict, Optional

import numpy as np
import pytesseract
from cv2 import cv2
from langdetect import detect_langs
from pdfplumber import page
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

from ai_data_preprocessing_queue.services.image_file_services import scale_too_big_cv2_image, scale_too_big_image

LANG_MAPPING = {"deu": "de", "eng": "en", "rus": "ru", "spa": "sp"}


def step(item: Any, itemState: Dict[str, Any], globalState: Optional[Dict[str, Any]], preprocessorData: str) -> Any:
    text = ""

    if type(item) == np.ndarray or type(item) == JpegImageFile:
        params = {"lang": "deu", "config": "--psm 1"}

        if globalState and globalState.get("image_to_string", {}):
            params.update(globalState.get("image_to_string"))  # type: ignore

        if type(item) == JpegImageFile:
            scale_too_big_image(item, params.get("cut_of_size", None))  # type: ignore
        else:
            scale_too_big_cv2_image(item, params.get("cut_of_size", None))  # type: ignore

        _text = str((pytesseract.image_to_string(item, lang=params.get("lang"), config=params.get("config"))))
        best_prob = 0

        for _ in range(0, 4):
            langs = detect_langs(_text[:100])
            language = langs[0].lang
            prob = langs[0].prob

            if language == LANG_MAPPING.get(params.get("lang")):  # type: ignore
                text = _text
                break

            if prob > best_prob:
                best_prob = prob
                text = _text

            if type(item) == np.ndarray:
                item = cv2.rotate(item, cv2.ROTATE_90_CLOCKWISE)
            if type(item) == JpegImageFile:
                item.transpose(Image.ROTATE_90)
            _text = str((pytesseract.image_to_string(item, lang=params.get("lang"), config="--psm 6")))

    elif type(item) == page.Page:
        text = item.extract_text()

    return text
