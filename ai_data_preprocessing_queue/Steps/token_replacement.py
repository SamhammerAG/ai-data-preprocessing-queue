import re
from typing import Any, Dict, List, Optional


# the higher the number the higher the prio
def step(item: Any, itemState: Dict[str, Any], globalState: Optional[Dict[str, Any]], preprocessorData: str) -> Any:
    if preprocessorData is None or not preprocessorData:
        return item

    lines = _get_data_from_store_or_reload(globalState, preprocessorData)

    for line in lines:
        escaped = re.escape(line[0])
        regex = "\\b" + escaped

        # also replace dots at end of word
        if not line[0].endswith("."):
            regex = regex + "\\b"

        pattern = re.compile(regex)
        item = pattern.sub(line[1], item)

    return item


def _get_data_from_store_or_reload(globalState: Optional[Dict[str, Any]], preprocessorData: str) -> List[List[str]]:
    if globalState is None:
        return _prepare_pre_processor_data(preprocessorData)

    dictIdentifier = "tokenReplacementPreprocessorData"
    if dictIdentifier in globalState:
        return globalState[dictIdentifier]

    preparedData = _prepare_pre_processor_data(preprocessorData)
    globalState[dictIdentifier] = preparedData
    return preparedData


def _prepare_pre_processor_data(preprocessorData: str) -> List[List[str]]:
    lines: List[List[str]] = [
        [s.strip() for i, s in enumerate(line.split(",")) if (i == 2 and re.compile(r"^[0-9\s]+$").match(s)) or i < 2]
        for line in preprocessorData.splitlines()
        if line.count(",") == 2
    ]
    lines = [line for line in lines if len(line) == 3]

    i: int = 0
    while i < len(lines):
        lines[i][2] = int(lines[i][2])  # type: ignore
        i += 1

    # sort
    lines = sorted(lines, key=lambda f: 0 - f[2])  # type: ignore

    return lines
