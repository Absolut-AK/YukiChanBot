def getRarity(item):
    common = ['blueMushroom', 'redMushroom', 'blackMushroom',
     'whiteMushroom', 'yellowMushroom', 'greenMushroom', 'coal', 'smallFish', 'freshWater', 'rock', 'insect']
    uncommon = ['sulfur', 'iron', 'mediumFish']
    rare = ['gold', 'bigFish']
    epic = ['hugeFish']
    for i in common:
        if item == i:
            return 'common'
    for i in uncommon:
        if item == i:
            return 'uncommon'
    for i in rare:
        if item == i:
            return 'rare'
    for i in epic:
        if item == i:
            return 'epic'
    
    

    
