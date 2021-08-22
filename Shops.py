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
        elif rarity == 'uncommon':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (10*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
        elif rarity == 'rare':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (25*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
        elif rarity == 'epic':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (50*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
        elif rarity == 'legendary':
            coins = getDataValue(id, 'coin')
            inserting(id, 'coin', coins + (500*ammount))
            itemVal = getInvValue(id, item)
            invInsert(id, item, itemVal-ammount)
        elif rarity == 'ruby':
            pass
        elif rarity == 'saphire':
            pass
        elif rarity == 'mythic':
            pass
    else:
        return "You don't have that item" 