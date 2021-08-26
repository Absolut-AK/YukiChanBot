from jsonDatabase import *
from fightingSystem import userStats
def xpNeeded(lvl):
    return round((4 * (lvl ** 3 )) / 5)

def levelUp(id, lvl, exp):
    xpNeed = xpNeeded(lvl)
    while exp >= xpNeed:
        inserting(id, 'level', lvl+1)
        tempExp = getDataValue(id, 'exp')
        inserting(id, 'exp', tempExp - xpNeeded(lvl))
        power = getDataValue(id, 'power')
        hp = getDataValue(id, 'hp')
        speed = getDataValue(id, 'speed')
        endurance = getDataValue(id, 'endurance')
        stamina = getDataValue(id, 'stamina')
        if getDataValue(id, 'class') == 'swordsman':
            inserting(id, 'power', power + 5)
            inserting(id, 'hp', hp + 10)
            inserting(id, 'speed', speed + 5)
            inserting(id, 'endurance', endurance + 10)
            return True
        elif getDataValue(id, 'class') == 'archer':
            inserting(id, 'power', power + 10)
            inserting(id, 'hp', hp + 5)
            inserting(id, 'speed', speed + 10)
            inserting(id, 'endurance', endurance + 5)
            return True
        elif getDataValue(id, 'class') == 'mage':
            inserting(id, 'power', power + 10)
            inserting(id, 'hp', hp + 10)
            inserting(id, 'speed', speed + 5)
            inserting(id, 'endurance', endurance + 5)
            return True
        exp = getDataValue(id, 'exp')
        lvl = getDataValue(id, 'level')
        xpNeed = xpNeeded(lvl)
        userStats(id)
    return False

def mobXp(lvl):
    return round((4 * (lvl ** 3)) / 103) + 1

