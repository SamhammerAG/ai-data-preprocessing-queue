import re


# the higher the number the higher the prio
def step(item: str, itemState: dict, globalState: dict, preprocessorData: str) -> str:
    if preprocessorData is None or preprocessorData == "":
        return item

    lines = _get_data_from_store_or_reload(globalState, preprocessorData)

    for l in lines:
        escaped = re.escape(l[0])
        regex = "\\b" + escaped

        # also replace dots at end of word
        if not l[0].endswith('.'):
            regex = regex + "\\b"

        pattern = re.compile(regex)
        item = pattern.sub(l[1], item)

    return item


def _get_data_from_store_or_reload(globalState: dict, preprocessorData: str) -> [[str]]:
    if globalState is not None:
        dictIdentifier = "tokenReplacementPreprocessorData"
        if dictIdentifier not in globalState:
            preparedData = _prepare_pre_processor_data(preprocessorData)
            globalState[dictIdentifier] = preparedData
            return preparedData
        else:
            return globalState[dictIdentifier]
    else:
        return _prepare_pre_processor_data(preprocessorData)


def _prepare_pre_processor_data(preprocessorData: str) -> [[str]]:
    lines = [[s.strip() for i, s in enumerate(l.split(",")) if (i == 2 and re.compile(r"^[0-9\s]+$").match(s)) or i < 2] for l in preprocessorData.splitlines() if l.count(",") == 2]
    lines = [l for l in lines if len(l) == 3]

    i = 0
    while i < len(lines):
        lines[i][2] = int(lines[i][2])
        i += 1

    # sort
    sortFn = lambda i: 0 - i[2]
    lines = sorted(lines, key=sortFn)

    return lines
