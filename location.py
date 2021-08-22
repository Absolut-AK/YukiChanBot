import random
from jsonDatabase import invInsert, getInvKey, getInvValue
def locations(id, location):
    if location == 'forest':
        return forest(id)
    elif location == 'cave':
        return cave(id)
    elif location == 'river':
        return river(id)
    elif location == 'lake':
        return lake(id)
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
    items = ['gold', 'iron', 'coal', 'sulfur', 'coal', 'iron']
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
def lake(id):
    items = ['smallFish', 'mediumFish', 'bigFish', 'hugeFish', 'smallFish', 'smallFish', 'mediumFish', 'mediumFish', 'bigFish']
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
def river(id):
    items = ['freshWater', 'rocks', 'smallFish', 'insect', 'rocks', 'freshWater']
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