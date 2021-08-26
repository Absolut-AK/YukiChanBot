from jsonDatabase import *
from profileStats import restOfProfile
from fightingSystem import userStats
def guildSignup(id, msg):
    if msg.content.lower() == 'y' or msg.lower == 'yes':
        if getDataValue(id, 'coin') >= 100:
            value = getDataValue(id, 'coin') - 100
            inserting(id, 'coin', value)
            inserting(id, 'guild', True)
            restOfProfile(id)
            userStats(id)
            insertingDic(id, 'enemy')
            return 'Now you are registrated!!'
        else:
            return "Looks like you don't got enough"
    else:
        return "Okay, maybe later then"