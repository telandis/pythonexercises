def count_seven_solution(number):
    track = number
    count = 0
    while track > 0:
        if track % 10 == 7:
            count += 1
        track //= 10
    return count
