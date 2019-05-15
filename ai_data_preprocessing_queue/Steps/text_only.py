import re


def step(item, itemState, globalState, preprocessorData: str):
    item = re.sub(r'[^\w\s]', ' ', item)
    item = re.sub(r"""\d""", ' ', item)
    return item
