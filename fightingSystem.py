import random
from jsonDatabase import *
from mobs import *
from abilities import abilities
#fightingSystem

#Stage
def enemys(id, floor):
    enemy1 = defaultMob(floor)
    hp, power, speed, endurance = enemy1
    print(type(endurance))
    insertingDic(id, 'enemy')
    insertInDic(id, 'enemy', 'hp', hp)
    insertInDic(id, 'enemy', 'power', power)
    insertInDic(id, 'enemy', 'speed', speed)
    insertInDic(id, 'enemy', 'endurance', endurance)
    print(hp, power, speed, type(endurance))

def userStats(id):
    insertingDic(id, 'userStats')
    hp = getDataValue(id, 'hp')
    power = getDataValue(id, 'power')
    speed= getDataValue(id, 'speed')
    endurance = getDataValue(id, 'endurance')
    stamina = getDataValue(id, 'stamina')
    insertInDic(id, 'userStats', 'hp', hp)
    insertInDic(id, 'userStats', 'power', power)
    insertInDic(id, 'userStats', 'speed', speed)
    insertInDic(id, 'userStats', 'endurance', endurance)
    insertInDic(id, 'userStats', 'stamina', stamina)

def fight(id, ability=1):
    ability = ability.content.lower()
    ability = abilities(id, ability)
    user = openNewDic(id, 'userStats')
    enemy = openNewDic(id, 'enemy')
    print(enemy['hp'])
    if user['speed'] >= enemy['speed']:
        enemy['hp'] = enemy['hp'] - ((user['power'] * ability) - enemy['endurance'])
        user['hp'] = user['hp'] - (enemy['power'] - user['endurance'])
    elif enemy['speed'] >= user['speed']:
        user['hp'] = user['hp'] - (enemy['power'] - user['endurance'])
        enemy['hp'] = enemy['hp'] - ((user['power'] * ability) - enemy['endurance'])
    
    insertInDic(id, 'enemy', 'hp', enemy['hp'])
    insertInDic(id, 'userStats', 'hp', user['hp'])

    return f"Enemy's health: {enemy['hp']}\n Your health: {user['hp']}"