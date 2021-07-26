import random
cardPoints = [
2, 2, 2, 2,
3, 3, 3 ,3,
4, 4, 4, 4,
5, 5, 5, 5, 
6, 6, 6, 6,
7, 7, 7, 7,
8, 8, 8, 8,
9, 9, 9, 9,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
'a', 'a', 'a', 'a', 
2, 2, 2, 2,
3, 3, 3 ,3,
4, 4, 4, 4,
5, 5, 5, 5, 
6, 6, 6, 6,
7, 7, 7, 7,
8, 8, 8, 8,
9, 9, 9, 9,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
'a', 'a', 'a', 'a']
playerCards = []
computerCards = []
compSum = 0
playerSum = 0 

def blackJack():
    global cardPoints
    #shuffle
    if len(cardPoints) <= 26:
        cardPoints = [
        2, 2, 2, 2,
        3, 3, 3 ,3,
        4, 4, 4, 4,
        5, 5, 5, 5, 
        6, 6, 6, 6,
        7, 7, 7, 7,
        8, 8, 8, 8,
        9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        'a', 'a', 'a', 'a', 
        2, 2, 2, 2,
        3, 3, 3 ,3,
        4, 4, 4, 4,
        5, 5, 5, 5, 
        6, 6, 6, 6,
        7, 7, 7, 7,
        8, 8, 8, 8,
        9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        'a', 'a', 'a', 'a']
        print("dealer shuffeling")
    #bustedCheck
    def busted(sum):
        if sum > 21:
            print("busted")
            leaveOrStay()
        if sum < 21:
            return False

    #blackJack for player
    def natural(hand):
        hand = aceSwitch(playerCards)
        if hand == 21:
            print("blackJack")
            leaveOrStay()

    # wincondition
    def winCondition():
        global compSum, playerSum
        if compSum == playerSum:
            print('draw')
            leaveOrStay()
        elif compSum > playerSum and compSum <= 21:
            print('dealer win')
            leaveOrStay()
        elif playerSum > compSum and playerSum <= 21:
            print('you win')
            leaveOrStay()
    
    #computerRules
    def computerCheck():
        global compSum
        if compSum > 16:
            winCondition()

    #drawCard
    def drawCard(numb):
        drawCards = []
        for i in range(numb):
            draw = random.choice(cardPoints)
            drawCards.append(draw)
            cardPoints.remove(draw)
        return drawCards

    #sumWithAce
    def aceSwitch(cardList):
            add = 0
            subList = []
            for i in range(0, len(cardList)):
                if cardList[i] == 11:
                    subList.append(1)
                elif 'a' not in cardList:
                    add = sum(cardList) 
                else:
                    for i in range(0, len(cardList)):
                        subList.append(i)
                    for i in range(0, len(subList)):
                        add += subList[i]          
            return add

    #2cards each
    def firstCards():
        twoCards = drawCard(2)
        return twoCards

    #start of game
    def start():
        global playerCards, computerCards
        playerCards = []
        computerCards = []
        playerCards += firstCards()
        natural(playerCards)
        computerCards += firstCards()
        print(f"Dealer cards are x & {computerCards[1]} \n Your cards are {playerCards[0]} & {playerCards[1]}")
        print("Do you want to hit?")
        hitOrNot()

    #desisions
    def hitOrNot():
        print("yes or no y/n")
        yn = input()
        if yn == 'y':
            hit()
        elif yn == 'n':
            stay()
        else:
            hitOrNot()

    def leaveOrStay():
        print("you want to leave the table?")
        yn = input()
        if yn == 'y':
            print("Thank you for playing")
        elif yn == 'n':
            start()
        else:
            leaveOrStay()
    #hit
    def hit():
        global playerCards, playerSum
        playerCards += drawCard(1)
        print(playerCards)
        playerSum = aceSwitch(playerCards)
        if busted(playerSum) == False:
            hitOrNot()

    #stay
    def stay():
        global compSum, computerCards, playerSum, playerCards
        compSum = aceSwitch(computerCards)
        playerSum = aceSwitch(playerCards)
        print(computerCards)
        if compSum <= 21 and compSum > playerSum :
            winCondition()
        else:
            computerCards += drawCard(1)
            computerCheck()
            if busted(compSum) == False:
                stay()
    start()
blackJack()


