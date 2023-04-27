from typing import Any, Dict, Optional

from langdetect import detect

"""
Detects one of the following languages and writs the language to local state
af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi,
zh-cn, zh-tw
"""


def step(item: Any, itemState: Dict[str, Any], globalState: Optional[Dict[str, Any]], preprocessorData: str) -> Any:
    itemState["language"] = detect(item[:100])
    return item
