from jsonDatabase import *
def abilities(id, abilityNum):
    print(abilityNum)
    abilityName = getDicValue(id, 'abilities', abilityNum)
    if abilityName == "normal":
        return 1

def ability(id):
    text = ''
    abilities = openNewDic(id, 'abilities')
    for key, value in abilities.items():
        text += f'{key}: {value} \n'
    return text
print(ability(288623940404772865))