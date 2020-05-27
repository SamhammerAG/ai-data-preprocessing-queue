import re


def step(item, itemState, globalState, preprocessorData: str):
    item = re.sub(r'[^\w\s]', ' ', item)
    return item