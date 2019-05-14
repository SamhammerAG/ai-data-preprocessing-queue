import glob
from typing import List
from io import TextIOWrapper
import numpy

# TODO: can this be cached? what about users environments etc
lines: List[List[str]] = []

# the higher the number the higher the prio
def step(item: str, itemState: dict, globalState: dict) -> str:
    global lines
    tokenDir: str = globalState.get("tokenDir")

    for file in glob.glob(tokenDir + "/*.csv"):
        handler: TextIOWrapper = open(file, "r")
        header = [f.strip() for f in handler.readline().split(",")]

        if (header[0] != "abbreviation" or header[1] != "full" or header[2] != "sort"):
            handler.close()
            raise Exception("header does not match, maybe your file is not the right one")
        
        lines = [[s.strip() for s in l.split(",")] for l in handler.readlines()]
        
        i = 0
        while i < len(lines):
            lines[i][2] = int(lines[i][2])
            i += 1

        handler.close()

        # sort
        sortFn = lambda i: 0 - i[2]
        sortedList = sorted(lines, key = sortFn)

        print(sortedList)

    return item