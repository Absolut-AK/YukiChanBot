from jsonDatabase import *
def guildSignup(id, msg):
    print(msg.content.lower())
    if msg.content.lower() == 'y' or msg.lower == 'yes':
        if getDataValue(id, 'coin') >= 100:
            value = getDataValue(id, 'coin') - 100
            inserting(id, 'coin', value)
            inserting(id, 'guild', True)
            return 'Now you are registrated!!'
        else:
            return "Looks like you don't got enough"
    else:
        return "Okay, maybe later then"