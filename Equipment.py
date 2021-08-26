from jsonDatabase import *
import random
def equip(id, artifact):
    insertingInArtifacts(id, artifact, openArtifactsInv(id, artifact))

def upgrades(id, artifact):
    rarity = openArtifacts(id, artifact)['rarity']
    rarityArtifact = {'common': 1, 'uncommon': 2, 'rare': 3, 'epic': 4, 'legendary': 5, "lapiz": 6, "iron": 7, "gold": 8, "ruby": 9, "saphire": 10, "diamond":11}
    if getDataValue(id, 'coin') >= rarityArtifact[rarity] * 500:
        coin = getDataValue(id, 'coin')
        coin -= rarityArtifact[rarity] * 500
        inserting(id, 'coin', coin)
        artifactDic = openArtifacts(id, artifact)
        stats = []
        for i in range(len(artifactDic)):
            if 'speed' in artifactDic:
                stats.append("speed")
            if 'stamina' in artifactDic:
                stats.append("stamina")
            if 'endurance' in artifactDic:
                stats.append("endurance")
            if 'hp' in artifactDic:
                stats.append("hp")
            if 'power' in artifactDic:
                stats.append("power")
        randomStats = random.choice(stats)
        print(stats)
        print(randomStats)
        if randomStats == "power":
            power = rarityArtifact[rarity] * 20
            power += openArtifacts(id, artifact)['power']
            editArtifact(id, artifact, 'power', power)
        elif randomStats == "hp":
            hp = rarityArtifact[rarity] * 30
            hp += openArtifacts(id, artifact)['hp']
            editArtifact(id, artifact, 'power', hp)
        elif randomStats == "endurance":
            endurance = rarityArtifact[rarity] * 5
            endurance += openArtifacts(id, artifact)['endurance']
            editArtifact(id, artifact, 'power', endurance)
        elif randomStats == "stamina":
            stamina = rarityArtifact[rarity] * 2
            stamina += openArtifacts(id, artifact)['stamina']
            editArtifact(id, artifact, 'power', stamina)
        elif randomStats == "speed":
            speed = rarityArtifact[rarity] * 10
            speed += openArtifacts(id, artifact)['speed']
            editArtifact(id, artifact, 'power', speed)
        
    else:
        return "You don't have enough coins"
    return "Upgraded"
