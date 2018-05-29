
def pairs(input):
    """input is a list of ints; output is a list of unique tuple pairs"""
    # Solution goes here
    tuplist = []
    if len(input) < 2:
        return tuplist

    for x in range(0, len(input)):
        for y in range(x+1, len(input)):
            tuplist.append((input[x], input[y]))

    return tuplist


def is_four_of_kind(hand):
    """hand is a list of 5 strings representing card ranks; function is a predicate"""
    # Solution goes here
    handdict = {}
    for card in hand:
        count = handdict.get(card,0)
        handdict[card] = count + 1

    for card in handdict:
        if handdict[card] >= 4:
            return True

    return False

def merge(a, b):
    """a and b are sorted list of ints; function returns array of sorted ints"""
    # Solution goes here
    aIndex = 0
    bIndex = 0
    sorted = []
    while len(sorted) != len(a) + len(b):
        #if one list is empty then just add remaining values in other list to sorted list
        if aIndex >= len(a):
            sorted.append(b[bIndex])
            bIndex += 1
            continue

        if bIndex >= len(b):
            sorted.append(a[aIndex])
            aIndex += 1
            continue
        ####

        #merge
        if a[aIndex] < b[bIndex]:
            sorted.append(a[aIndex])
            aIndex += 1
        elif a[aIndex] > b[bIndex]:
            sorted.append(b[bIndex])
            bIndex += 1
        else:
            sorted.append(a[aIndex])
            aIndex += 1
            sorted.append(b[bIndex])
            bIndex += 1

    return sorted

def dec_to_base_x(base, num):
    """function that converts base 10 number to a number of base from 2 to 9 and returns its STRING representation"""
    # Solution goes here
    if base > 10 or base < 2:
        return None

    if base == 10:
        return str(num)

    newNum = ""
    quot = num//base
    remainder = num%base
    newNum = str(remainder) + newNum
    while quot > 0:
        remainder = quot%base
        quot = quot//base
        newNum = str(remainder) + newNum

    #if remainder == 0:

    return newNum
