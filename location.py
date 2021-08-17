import random
from jsonDatabase import invInsert, getInvKey, getInvValue
def locations(id, location):
    if location == 'forest':
        return forest(id)
    elif location == 'easteregg':
        return 'sheeeshh u found me~'
def forest(id):
    items = ['blueMushroom', 'redMushroom', 'blackMushroom', 'whiteMushroom', 'yellowMushroom', 'greenMushroom']
    randomItem = random.choice(items)
    if getInvKey(id, randomItem):
        value = getInvValue(id, randomItem)
        print(value)
        value += 1
        print(value)
        invInsert(id, randomItem, value)
    else:
        invInsert(id, randomItem, 1)
    return f'You found {randomItem} x1'
def cave(id):
    pass
def lake(id):
    pass
def river(id):
    pass