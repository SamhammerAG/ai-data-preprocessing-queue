import re


# the higher the number the higher the prio
def step(item: str, itemState: dict, globalState: dict, preprocessorData: str) -> str:

    lines = [[s.strip() for i, s in enumerate(l.split(",")) if (i == 2 and re.compile(r"^[0-9\s]+$").match(s)) or i < 2] for l in preprocessorData.splitlines() if l.count(",") == 2]
    lines = [l for l in lines if len(l) == 3]

    i = 0
    while i < len(lines):
        lines[i][2] = int(lines[i][2])
        i += 1

    # sort
    sortFn = lambda i: 0 - i[2]
    lines = sorted(lines, key=sortFn)

    for l in lines:
        item = item.replace(l[0], l[1])

    return item
