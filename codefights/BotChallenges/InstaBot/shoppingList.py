import re
def shoppingList(items):
    total = 0
    for match in re.finditer(r'(\d+(\.\d+)?)', items):
        s = match.start()
        e = match.end()
        total+=float(items[s:e])
    return total