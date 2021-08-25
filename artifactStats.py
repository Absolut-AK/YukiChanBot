from jsonDatabase import *
import random
def insertToArtifactInv(id, rarity, artifact):
    rarityArtifact = {'common': 1, 'uncommon': 2, 'rare': 3, 'epic': 4, 'legendary': 5, "lapiz": 6, "iron": 7, "gold": 8, "ruby": 9, "saphire": 10, "diamond":11}
    statList = ["power", "speed", "endurance", "stamina", "hp"]
    if rarityArtifact[rarity]:
        numS = rarityArtifact[rarity]
        insertingInArtifactsInv(id, artifact, 'rarity', rarity)
        while numS > 0:
            randomStats = random.choice(statList)
            rarityNum = rarityArtifact[rarity]
            if randomStats == 'power':
                insertingInArtifactsInv(id, artifact, randomStats, rarityNum * 20) 
            elif randomStats == 'speed':
                insertingInArtifactsInv(id, artifact, randomStats, rarityNum * 10)  
            elif randomStats == 'endurance':
                insertingInArtifactsInv(id, artifact, randomStats, rarityNum * 5)  
            elif randomStats == 'stamina':
                insertingInArtifactsInv(id, artifact, randomStats, rarityNum * 2)  
            elif randomStats == 'hp':
                insertingInArtifactsInv(id, artifact, randomStats, rarityNum * 30)  
            numS -= 1

def sellArtifact(id, rarity, ammount=1):
    coin = getDataValue(id, 'coin')
    if rarity == 'common':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (5*ammount))
        coin = 5*ammount
        return f"You earned {coin} coin"
    elif rarity == 'uncommon':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (10*ammount))
        coin = 10*ammount
        return f"You earned {coin} coin"
    elif rarity == 'rare':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (25*ammount))
        coin = 25*ammount
        return f"You earned {coin} coin"
    elif rarity == 'epic':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (50*ammount))
        coin = 50*ammount
        return f"You earned {coin} coin"
    elif rarity == 'legendary':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (500*ammount))
        coin = 500*ammount
        return f"You earned {coin} coin"
    elif rarity == 'lapiz':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (550*ammount))
        coin = 550*ammount
    elif rarity == 'iron':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (600*ammount))
        coin = 600*ammount
    elif rarity == 'gold':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (700*ammount))
        coin = 700*ammount
    elif rarity == 'ruby':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (800*ammount))
        coin = 800*ammount
    elif rarity == 'saphire':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (900*ammount))
        coin = 900*ammount
    elif rarity == 'mythic':
        coins = getDataValue(id, 'coin')
        inserting(id, 'coin', coins + (1000*ammount))
        coin = 1000*ammount

def userArtifacts(id):
    text = ''
    test = openArtifactsAll(id)
    for key, value in test.items():
        text += f"{key}: \n"
        for key, value in value.items():
            text += f"\t{key}: {value} \n"
    return text