def multipleThreeAndFive():
    start = 3
    total = 0
    while start < 1000:
        if start % 3 == 0 or start % 5 == 0:
            total += start
        start += 1
    return total
