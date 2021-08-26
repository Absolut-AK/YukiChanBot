from rarities import getRarity
from jsonDatabase import *
def sells(id, item, ammount=1):
    if getInvValue(id, item) >= ammount:
        rarity = getRarity(item)
        if rarity == 'common':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (5*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
            coin = 5*ammount
            return f"You earned {coin} coin"
        elif rarity == 'uncommon':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (10*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
            coin = 10*ammount
            return f"You earned {coin} coin"
        elif rarity == 'rare':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (25*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
            coin = 25*ammount
            return f"You earned {coin} coin"
        elif rarity == 'epic':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (50*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
            coin = 50*ammount
            return f"You earned {coin} coin"
        elif rarity == 'legendary':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (500*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
            coin = 500*ammount
            return f"You earned {coin} coin"
        elif rarity == 'lapiz':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (550*ammount))
            coin = 550*ammount
        elif rarity == 'iron':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (600*ammount))
            coin = 600*ammount
        elif rarity == 'gold':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (700*ammount))
            coin = 700*ammount
        elif rarity == 'ruby':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (800*ammount))
            coin = 800*ammount
        elif rarity == 'saphire':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (900*ammount))
            coin = 900*ammount
        elif rarity == 'mythic':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (1000*ammount))
            coin = 1000*ammount
        else:
            return "You don't have that item" 

def shopList():
    return '''Tools \n \tpickaxe: 1000 \n \tfishingrod: 1000 \n Abilities \n \t ability2: 3000 \n \t ability3: 10000 \n \tability4: 20000'''

def buy(id, item):
    if item.lower() == 'pickaxe':
        if getDataValue(id, 'coin') >= 1000:
            coins = getDataValue(id, 'coin')
            coins -= 1000
            inserting(id, 'pickaxe', 50)
            inserting(id, 'coin', coins)
            return "You bought a pickaxe"
        else:
            return "You don't have enough coins"
    elif item.lower() == 'fishingrod':
        if getDataValue(id, 'coin') >= 1000:
            coins = getDataValue(id, 'coin')
            coins -= 1000
            inserting(id, 'fishingrod', 50)
            inserting(id, 'coin', coins)
            return "You bought a fishingrod"
        else:
            return "You don't have enough coins"
    elif item.lower() == 'ability2':
        if getDataValue(id, 'coin') >= 3000:
            coins = getDataValue(id, 'coin')
            coins -= 3000
            insertInDic(id, 'abilities', 2, 'impovered')
            inserting(id, 'coin', coins)
            return "You bought a impovered ability"
        else:
            return "You don't have enough coins"
    elif item.lower() == 'ability3':
        if getDataValue(id, 'coin') >= 10000:
            coins = getDataValue(id, 'coin')
            coins -= 3000
            insertInDic(id, 'abilities', 3, 'legendary')
            inserting(id, 'coin', coins)
            return "You bought a legendary ability"
        else:
            return "You don't have enough coins"
    elif item.lower() == 'ability4':
        if getDataValue(id, 'coin') >= 20000:
            coins = getDataValue(id, 'coin')
            coins -= 3000
            insertInDic(id, 'abilities', 4, 'mythical')
            inserting(id, 'coin', coins)
            return "You bought a mythical ability"
        else:
            return "You don't have enough coins"