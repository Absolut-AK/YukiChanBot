import json, discord
from profileStats import creatingUserStats
def starterClass(msg, id):
    if msg.content.lower() == "swordsman" or msg.content.lower() == "s":
        creatingUserStats(id)
        return "you picked swordsman"
    elif msg.content.lower() == "archer" or msg.content.lower() == "a":
        creatingUserStats(id)
        return "you picked archer"
    elif msg.content.lower() == "mage" or msg.content.lower() == "m":
        creatingUserStats(id)
        return "you picked mage"
    else:
        return "you didn't pick anything"