from jsonDatabase import getDataKey, check
from profileStats import creatingUserClass
def starterClass(msg, id):
    check(id)
    if getDataKey(id, 'class'):
        return "You already have a class"
    else:
        if msg.content.lower() == "swordsman" or msg.content.lower() == "s":
            creatingUserClass(id, "swordsman")
            return "you picked swordsman. (ノ*°▽°*)"
        elif msg.content.lower() == "archer" or msg.content.lower() == "a":
            creatingUserClass(id, "archer")
            return "you picked archer. (⁄ ⁄•⁄ω⁄•⁄ ⁄)"
        elif msg.content.lower() == "mage" or msg.content.lower() == "m":
            creatingUserClass(id, "mage")
            return "you picked mage („ಡωಡ„)"
        else:
            return "you didn't pick anything ┌∩┐(◣_◢)┌∩┐"