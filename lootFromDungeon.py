import random
from levelSystem import *
def coinGain(id, floor):
    coin = getDataValue(id, 'coin')
    coin += int(floor) * 5
    inserting(id, 'coin', coin)
    return int(floor) * 5

def xpGain(id, floor):
    floor = int(floor)
    xp = round(xpNeeded(floor) / 3) + floor
    savedXp = xp
    xp = xp + getDataValue(id, 'exp')
    inserting(id, 'exp', xp)
    return savedXp

def lootRarity(floor):
    floor = int(floor)
    if floor <= 10:
        return ["common"]
    elif floor <= 20:
        return ["common", "uncommon"]
    elif floor <= 30:
        return ["common", "uncommon", "rare"]
    elif floor <= 40:
        return ["common", "uncommon", "rare", "epic"]
    elif floor <= 50:
        return ["common", "uncommon", "rare", "epic", "legendary"]
    elif floor <= 60:
        return ["common", "uncommon", "rare", "epic", "legendary", "lapiz"]
    elif floor <= 70:
        return ["common", "uncommon", "rare", "epic", "legendary", "lapiz", "iron"]
    elif floor <= 80:
        return ["common", "uncommon", "rare", "epic", "legendary", "lapiz", "iron", "gold"]
    elif floor <= 90:
        return ["common", "uncommon", "rare", "epic", "legendary", "lapiz", "iron", "gold", "ruby"]
    elif floor <= 100:
        return ["common", "uncommon", "rare", "epic", "legendary", "lapiz", "iron", "gold", "ruby", "saphire"]
    elif floor <= 110:
        return ["common", "uncommon", "rare", "epic", "legendary", "lapiz", "iron", "gold", "ruby", "saphire", "diamond"]
def lootGain(id, floor):
    rarity = lootRarity(floor)
    randomRarity = random.choice(rarity)
    lootItems = ['ring', 'hat', 'gloves', 'weapon', 'mask', 'shirt', 'pants']
    randomLoot = random.choice(lootItems)
    item = randomRarity + ' ' + randomLoot
    if getDicValue(id, 'artifacts', randomLoot) == None:
        insertInDic(id, 'artifacts', randomLoot, item)
    else:
        pass
    return randomRarity, randomLoot