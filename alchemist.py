from jsonDatabase import *

#healing potion

def healingPotion(id):
    if getInvValue(id, 'redMushroom') > 3:
        value1 = getInvValue(id, 'healingPotion') + 1
        invInsert(id, 'healingPotion', value1)
        value2 = getInvValue(id, 'redMushroom') - 3
        invInsert(id, 'redMushroom', value2)

#Mana potion
def healingPotion(id):
    if getInvValue(id, 'blueMushroom') > 3:
        value1 = getInvValue(id, 'manaPotion') + 1
        invInsert(id, 'manaPotion', value1)
        value2 = getInvValue(id, 'blueMushroom') - 3
        invInsert(id, 'blueMushroom', value2)
