from functools import reduce
from typing import Any, Dict, Optional, Set, cast

import numpy as np


def step(item: Any, itemState: Dict[str, Any], globalState: Optional[Dict[str, Any]], preprocessorData: str) -> Any:
    if preprocessorData is None:
        return item

    words = preprocessorData.splitlines()

    if not words:
        return item

    values = {len(w) for w in words}
    groupedReplaceWords = [{"key": key, "items": list(filter(lambda x: len(x) == key, words))} for key in values]
    allItemWords: Set[str] = set(item.split(" "))  # reduce all words
    # all words with more than 4 can have distance 2, al other 1

    for itemWord in allItemWords:
        if itemWord in words:
            continue

        length = len(itemWord)
        items = [x.get("items") for x in groupedReplaceWords if length - 2 <= cast(int, x.get("key")) <= length + 2]
        if not items:
            continue

        allWordsToCheck: Any = reduce(lambda x, y: cast(str, x) + cast(str, y), items)

        for w in allWordsToCheck:
            if len(itemWord) < 4 and _levenshtein(itemWord, w) == 1:
                item = item.replace(itemWord, w)
            elif len(itemWord) >= 4 and 1 <= _levenshtein(itemWord, w) <= 2:
                item = item.replace(itemWord, w)

    return item


def _levenshtein(seq1: str, seq2: str) -> int:
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1,
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1,
                )

    return matrix[size_x - 1, size_y - 1]
