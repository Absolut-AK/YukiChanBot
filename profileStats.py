from jsonDatabase import inserting, getDataValue, getInvData
from levelSystem import *

def creatingUserClass(id, c):
    if c == "swordsman":
        inserting(id, "class", 'swordsman')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 50)
        inserting(id, "hp", 120)
        inserting(id, "speed", 50)
        inserting(id, "endurance", 15)
        inserting(id, "stamina", 20)
        insertingDic(id, "abilities")
        insertingDic(id, "artifacts")
        insertingDic(id, "artifactInventory")
        insertingDic(id, "inventory")
    elif c == 'archer':
        inserting(id, "class", 'archer')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 55)
        inserting(id, "hp", 100)
        inserting(id, "speed", 60)
        inserting(id, "endurance", 10)
        inserting(id, "stamina", 20)
        insertingDic(id, "abilities")
        insertingDic(id, "artifacts")
        insertingDic(id, "artifactInventory")
        insertingDic(id, "inventory")
    elif c == 'mage':
        inserting(id, "class", 'mage')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 55)
        inserting(id, "hp", 100)
        inserting(id, "speed", 30)
        inserting(id, "endurance", 10)
        inserting(id, "stamina", 20)
        insertingDic(id, "abilities")
        insertingDic(id, "artifactInventory")
        insertingDic(id, "artifacts")
        insertingDic(id, "inventory")


def profileStats(id):
    level = getDataValue(id, "level")
    coin = getDataValue(id, "coin")
    power = getDataValue(id, "power")
    hp = getDataValue(id, "hp")
    speed = getDataValue(id, "speed")
    endurance = getDataValue(id, "endurance")
    stamina = getDataValue(id, "stamina")
    experience = getDataValue(id, "exp")
    nextLvlUp = xpNeeded(getDataValue(id, 'level'))
    for key, value in openArtifactsInvAll(id).items():
        for key, value in value.items():
            if value == 'power':
                power += value
            elif value == 'hp':
                hp += value
            elif value == 'speed':
                speed += value
            elif value == 'endurance':
                endurance += value
            elif value == 'stamina':
                stamina += value
            else:
                pass
    profileDescription = f"Level: {level} \n experience:{experience}/{nextLvlUp} \n Coin: {coin} \n Power: {power} \n Health: {hp} \n Speed: {speed} \n Endurance: {endurance} \n Mana/Stamina: {stamina}"
    return profileDescription

def inventorys(id):
    text = getInvData(id)
    return text

def restOfProfile(id):
    insertInDic(id, "abilities", "1", "normal")
    insertInDic(id, "abilities", "2", None)
    insertInDic(id, "abilities", "3", None)
    insertInDic(id, "abilities", "4", None)
    insertInDic(id, "artifacts", "weapon", {"rarity": "starter"})
    insertInDic(id, "artifacts", "hat", {})
    insertInDic(id, "artifacts", "mask", {})
    insertInDic(id, "artifacts", "shirt", {})
    insertInDic(id, "artifacts", "pants", {})
    insertInDic(id, "artifacts", "gloves", {})
    insertInDic(id, "artifacts", "boots", {})
    insertInDic(id, "artifacts", "ring", {})
    insertInDic(id, "artifactInventory", "weapon", {})
    insertInDic(id, "artifactInventory", "hat", {})
    insertInDic(id, "artifactInventory", "mask", {})
    insertInDic(id, "artifactInventory", "shirt", {})
    insertInDic(id, "artifactInventory", "pants", {})
    insertInDic(id, "artifactInventory", "gloves", {})
    insertInDic(id, "artifactInventory", "boots", {})
    insertInDic(id, "artifactInventory", "ring", {})
