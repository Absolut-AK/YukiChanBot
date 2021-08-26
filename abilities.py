from jsonDatabase import *
def abilities(id, abilityNum):
    abilityName = getDicValue(id, 'abilities', abilityNum)
    if abilityName == "normal":
        return 1
    elif abilityName == 'impovered':
        return 1.25
    elif abilityName == "legendary":
        return 2
    elif abilityName == "mythical":
        return 10

def ability(id):
    text = ''
    abilities = openNewDic(id, 'abilities')
    for key, value in abilities.items():
        text += f'{key}: {value} \n'
    return text