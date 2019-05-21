import re
from io import StringIO
import pandas


def step(item: str, itemState: dict, globalState: dict, preprocessorData: str):
    if preprocessorData is None or preprocessorData == "":
        return item

    csv = _get_data_from_store_or_reload(globalState, preprocessorData)

    for _, row in csv.iterrows():
        pattern = re.compile(row[0])
        item = pattern.sub(' ' + row[1] + ' ', item)

    return item


def _get_data_from_store_or_reload(globalState: dict, preprocessorData: str) -> pandas.DataFrame:
    if globalState is not None:
        dictIdentifier = "numberInterpretationPreprocessorData"
        if dictIdentifier not in globalState:
            preparedData = _prepare_pre_processor_data(preprocessorData)
            globalState[dictIdentifier] = preparedData
            return preparedData
        else:
            return globalState[dictIdentifier]
    else:
        return _prepare_pre_processor_data(preprocessorData)


def _prepare_pre_processor_data(preprocessorData: str) -> pandas.DataFrame:
    csv = pandas.read_csv(StringIO(preprocessorData), header=None, usecols=[0, 1, 2], quotechar='"', encoding="utf8")

    csv[0] = csv[0].str.strip()
    csv[1] = csv[1].str.strip()
    csv[2] = pandas.to_numeric(csv[2])
    csv["sort"] = csv[2]

    # sort
    return csv.sort_values("sort", inplace=False).drop("sort", "columns")
