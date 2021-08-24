from jsonDatabase import *
import random
def giveArtifactStats(id, rarity, artifact):
    rarityArtifact = {'common': 1, 'uncommon': 2, 'rare': 3, 'epic': 4, 'legendary': 5, }
    statList = ["power", "speed", "endurance", "stamina", "hp"]
    if rarityArtifact[rarity]:
        numS = rarityArtifact[rarity]
        insertingInArtifacts(id, artifact, 'rarity', rarity)
        while numS > 0:
            randomStats = random.choice(statList)
            rarityNum = rarityArtifact[rarity]
            if randomStats == 'power':
                insertingInArtifacts(id, artifact, randomStats, rarityNum * 20) 
            elif randomStats == 'speed':
                insertingInArtifacts(id, artifact, randomStats, rarityNum * 10)  
            elif randomStats == 'endurance':
                insertingInArtifacts(id, artifact, randomStats, rarityNum * 5)  
            elif randomStats == 'stamina':
                insertingInArtifacts(id, artifact, randomStats, rarityNum * 2)  
            elif randomStats == 'hp':
                insertingInArtifacts(id, artifact, randomStats, rarityNum * 30)  
            numS -= 1