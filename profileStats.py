from jsonDatabase import idIndexFinder
class Stats():
    def __init__(self, power, hp, speed, endurance, stamina):
        self.power = power
        self.hp = hp
        self.speed = speed
        self.endurance = endurance
        self.stamina = stamina
    def creation(self, id):
        pass

def creatingUserStats(id):       
        idIndex = idIndexFinder(id)

