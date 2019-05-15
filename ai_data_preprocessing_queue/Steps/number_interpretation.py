import re
import glob
from pathlib import Path
from .number_interpretation_preprocessor import BaseReplacer
from os.path import dirname
from typing import List
import pandas

def step(item, itemState, globalState):
    csv = pandas.read_csv(dirname(__file__)+"/../data/number_interpretation.csv", header=None, usecols=[0,1,2], quotechar='"')
    csv[0] = csv[0].str.strip()
    csv[1] = csv[1].str.strip()
    csv[2] = pandas.to_numeric(csv[2])
    csv["sort"] = csv[2]

    # sort
    csv = csv.sort_values("sort", inplace=False).drop("sort", "columns")

    for _, row in csv.iterrows():
        pattern = re.compile(row[0])
        item = pattern.sub(' ' + row[1] + ' ', item)

    return item