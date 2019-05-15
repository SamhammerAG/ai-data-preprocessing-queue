import glob
from typing import List
from io import TextIOWrapper
import numpy
import re

# the higher the number the higher the prio
def step(item: str, itemState: dict, globalState: dict, preprocessorData: str) -> str:

    lines = [[s.strip() for s in l.split(",")] for l in preprocessorData.splitlines()]
    
    i = 0
    while i < len(lines):
        lines[i][2] = int(lines[i][2])
        i += 1

    # sort
    sortFn = lambda i: 0 - i[2]
    lines = sorted(lines, key = sortFn)

    for l in lines:
        item = item.replace(l[0], l[1])

    return item