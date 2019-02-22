import re


def step(item, itemState, globalState):
    item = re.sub(r'[^\w\s]', ' ', item)
    item = re.sub(r"""\d""", ' ', item)
    return item
