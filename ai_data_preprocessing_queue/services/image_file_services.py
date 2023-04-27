from typing import Any

import cv2
from PIL import Image
from PIL.ImageOps import scale

CUTOFF_DEFAULT = 170000000  # 170 MPx
RESAMPLE = Image.BICUBIC
"""https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-filters
Available filters:
Filter      Downscaling quality     Upsacling quality   Performance

NEAREST                                                 *****
BOX         *                                           ****
Bilinear    *                       *                   ***
HAMMING     **                                          ***
[BICUBIC]   ***                     ***                 **              default
LANCZOS     ****                    ****                *
"""


def scale_too_big_image(image: Image, cutoff_size: int) -> Image:
    """Returns an rescaled image if it is larger than <cutoff_size> (in pixels)
    (default: 170 MPx) and an untouched image if it is smaller than <cutoff_size>.
    If <factor> is greater than 1, the image is scaled up. For values between 0 and 1
    the image is scaled down appropriately."""
    if not cutoff_size:
        cutoff_size = CUTOFF_DEFAULT
    _image_size = image.size[0] * image.size[1]
    if _image_size > cutoff_size:
        factor = cutoff_size / _image_size
        return scale(image, factor, RESAMPLE)
    return image


def scale_too_big_cv2_image(image: Any, cutoff_size: int) -> Any:
    if not cutoff_size:
        cutoff_size = CUTOFF_DEFAULT
    _image_size = image.shape[1] * image.shape[0]
    if _image_size > cutoff_size:
        factor = cutoff_size / _image_size
        width = int(image.shape[1] * factor)
        height = int(image.shape[0] * factor)
        dim = (width, height)
        return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image
