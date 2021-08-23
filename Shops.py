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
        elif rarity == 'ruby':
            pass
        elif rarity == 'saphire':
            pass
        elif rarity == 'mythic':
            pass
    else:
        return "You don't have that item" 

def shopList():
    return '''Tools \n \tpickaxe: 1000 \n \tfishingrod: 1000 \n Abilities \n \t NoneATM'''

def buy(id, item):
    if item.lower() == 'pickaxe':
        if getDataValue(id, 'coin') >= 1000:
            coins = getDataValue(id, 'coin')
            coins -= 1000
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