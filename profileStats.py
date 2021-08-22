from jsonDatabase import inserting, getDataValue, getInvData
from levelSystem import *

def creatingUserClass(id, c):
    if c == "swordsman":
        inserting(id, "class", 'swordsman')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 1)
        inserting(id, "hp", 15)
        inserting(id, "speed", 10)
        inserting(id, "endurance", 5)
        inserting(id, "stamina", 20)
        insertingDic(id, "abilities")
        insertingDic(id, "artifact")
        insertingDic(id, "inventory")
    elif c == 'archer':
        inserting(id, "class", 'archer')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 1)
        inserting(id, "hp", 15)
        inserting(id, "speed", 15)
        inserting(id, "endurance", 0)
        inserting(id, "stamina", 20)
        insertingDic(id, "abilities")
        insertingDic(id, "artifact")
        insertingDic(id, "inventory")
    elif c == 'mage':
        inserting(id, "class", 'mage')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 1)
        inserting(id, "hp", 10)
        inserting(id, "speed", 5)
        inserting(id, "endurance", 0)
        inserting(id, "stamina", 20)
        insertingDic(id, "abilities")
        insertingDic(id, "artifact")
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
    insertInDic(id, "artifacts", "weapon", "starter")
    insertInDic(id, "artifacts", "hat", None)
    insertInDic(id, "artifacts", "mask", None)
    insertInDic(id, "artifacts", "shirt", None)
    insertInDic(id, "artifacts", "pants", None)
    insertInDic(id, "artifacts", "gloves", None)
    insertInDic(id, "artifacts", "boots", None)
    insertInDic(id, "artifacts", "ring", None)