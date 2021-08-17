from jsonDatabase import inserting, getDataValue, getInvData
class Stats():
    def __init__(self, power, hp, speed, endurance, stamina):
        self.power = power
        self.hp = hp
        self.speed = speed
        self.endurance = endurance
        self.stamina = stamina
    def creation(self, id):
        pass

def creatingUserClass(id, c):
    if c == "swordsman":
        inserting(id, "class", 'swordsman')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 5)
        inserting(id, "hp", 15)
        inserting(id, "speed", 2)
        inserting(id, "endurance", 5)
        inserting(id, "stamina", 20)
    elif c == 'archer':
        inserting(id, "class", 'archer')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 5)
        inserting(id, "hp", 15)
        inserting(id, "speed", 3)
        inserting(id, "endurance", 0)
        inserting(id, "stamina", 20)
    elif c == 'mage':
        inserting(id, "class", 'mage')
        inserting(id, "level", 1)
        inserting(id, "coin", 0)
        inserting(id, "exp", 0)
        inserting(id, "power", 5)
        inserting(id, "hp", 10)
        inserting(id, "speed", 1)
        inserting(id, "endurance", 0)
        inserting(id, "stamina", 20)

def profileStats(id):
    level = getDataValue(id, "level")
    coin = getDataValue(id, "coin")
    power = getDataValue(id, "power")
    hp = getDataValue(id, "hp")
    speed = getDataValue(id, "speed")
    endurance = getDataValue(id, "endurance")
    stamina = getDataValue(id, "stamina")
    profileDescription = f"Level: {level} \n Coin: {coin} \n Power: {power} \n Health: {hp} \n Speed: {speed} \n Endurance: {endurance} \n Mana/Stamina: {stamina}"
    return profileDescription

def inventory(id):
    text = getInvData(id)
    return text
