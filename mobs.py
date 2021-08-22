import random
def dungeonLvl(floor):
    floor = int(floor)
    return round(random.randint(floor, floor + 2 )/ 3) +1

def defaultMob(floor):
    lvl = dungeonLvl(floor)
    ran = random.randint(lvl, lvl*2)
    hp = (round((lvl * (10 ** 2)/ 2)) + 1) + ran
    ran = random.randint(lvl, lvl*2)
    power = round((lvl * (10 ** 2/ 2)) + 1) + ran
    ran = random.randint(lvl, lvl*2)
    speed = ((lvl+5) * 20) + ran 
    endurance = ((lvl+5) * 20) + ran

    return hp, power, speed, endurance
    
def healtyDealerMob(lvl):
    pass

def dungeons():
    stages = random.randint(3, 8)
