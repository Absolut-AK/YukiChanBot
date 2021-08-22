from jsonDatabase import *
def abilities(id, abilityNum):
    print(abilityNum)
    abilityName = getDicValue(id, 'abilities', abilityNum)
    if abilityName == "normal":
        return 1