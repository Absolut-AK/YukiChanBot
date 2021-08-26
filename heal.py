from fightingSystem import userStats
from jsonDatabase import *
def healing(id):
    if getDataValue(id, 'coin') >= 100:
        userStats(id)
        coin = getDataValue(id, 'coin')
        coin -= 100
        inserting(id, 'coin', coin)
        return "Healed"
    else:
        return "You don't have enough money"