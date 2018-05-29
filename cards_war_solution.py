def cards_war_solution(cardsA, cardsB):
    # write your solution here
    aWins = 0
    for x in range(0, len(cardsA)):
        if getValue(cardsA[x]) > getValue(cardsB[x]):
            aWins += 1
            print(cardsA[x])
    return aWins

def getValue(card):
    if is_number(card):
        return int(card)
    elif card == 'T' or card == 't':
        return 10
    elif card == 'J' or card == 'j':
        return 11
    elif card == 'Q' or card == 'q':
        return 12
    elif card == 'K' or card == 'k':
        return 13
    else:#if A
        return 14

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
