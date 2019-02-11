import re


def step(item, globalState):
    item = re.sub(r'[^\w\s]', ' ', item)
    item = re.sub(r"""\d""", ' ', item)
    return item
