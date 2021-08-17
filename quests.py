import random
from jsonDatabase import getDataValue, inserting
def guess(gNum, difficulty, id):
    numbers = []
    for i in range(1, difficulty+1):
        numbers.append(i)
    ranNum = random.choice(numbers)
    coin = round(difficulty * 1)
    if gNum == ranNum:
        money = getDataValue(id, 'coin')
        inserting(id, 'coin', coin)
        text = f"You guessed it correct, you earned {coin} coins. ＼(￣▽￣)／"
        return text
    else:
        text = f"You gussed it wrong, my number was {ranNum}. (＃＞＜)"
        return text

def coinFlip(ammount, guess, id):
    ht = [1, 2]
    ranNum = random.choice(ht)
    coin = ammount * 2
    if ranNum == 1:
        hOrT = 'heads'
    else:
        hOrT = 'tails'
    if guess == hOrT:
        money = getDataValue(id, 'coin')
        money += ammount
        inserting(id, 'coin', money)
        return f"Guessed Right, earned {coin}coin. (❤ω❤)"
    else:
        money = getDataValue(id, 'coin')
        money -= ammount
        inserting(id, 'coin', money)
        return f"Guessed Wrong, lost {ammount}coin. (＞﹏＜)"
