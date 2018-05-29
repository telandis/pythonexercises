def reversing_coins_solution(coins):
	# write your solution here
    headsCount = 0
    tailsCount = 0
    for x in coins:
        if x == 0:
            headsCount += 1
        else:
            tailsCount += 1

    return headsCount if headsCount < tailsCount else tailsCount
