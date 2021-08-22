from jsonDatabase import *

#petShop
#pets
#petSystem

def petShops(name):
    if name == 'dog':
        return 'cost 1000coin, do you want to buy?'

def buyPets(id, name, msg):
    if msg.content.lower() == 'yes' or msg.content.lower() == 'y':
        if name == 'dog' and getDataValue(id, 'coin') >= 1000:
            inserting(id, 'coin', getDataValue(288623940404772865, 'coin') - 1000)
            if getDataKey(id, 'dog'):
                currentValue = getDataValue(id, 'dog')
                currentValue += 1
                inserting(id, 'dog', currentValue)
            else:
                inserting(id, 'dog', 1)
            return 'You bought a dog'
        else:
            return "You don't have enough coin"
    else:
        return 'Maybe next time'

print()