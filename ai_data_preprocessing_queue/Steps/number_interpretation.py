import re
import os
from io import StringIO
from os.path import dirname
import pandas


def step(item, itemState, globalState, preprocessorData: str):
    if preprocessorData is "":
        csvPath = os.path.join(dirname(__file__), "..", "data", "number_interpretation.csv")
        csv = pandas.read_csv(csvPath, header=None, usecols=[0, 1, 2], quotechar='"')
    else:
        csv = pandas.read_csv(StringIO(preprocessorData), header=None, usecols=[0, 1, 2], quotechar='"')

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
