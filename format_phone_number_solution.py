def format_phone_number_solution(string):
	# write your solution here
    numsOnly = pure_numbers(string)
    count = 0
    endOfNum = ""
    solution = ""
    if (len(numsOnly) % 3) == 0:
        endOfNum = numsOnly[len(numsOnly)-3:]
        numsOnly = numsOnly[:len(numsOnly)-3]
    elif (len(numsOnly) % 3) == 1:
        endOfNum = numsOnly[len(numsOnly)-4:len(numsOnly)-2] + "-" + numsOnly[len(numsOnly)-2:]
        numsOnly = numsOnly[:len(numsOnly)-4]
    else:#elif len(numsOnly) % 3) == 2
        endOfNum = numsOnly[len(numsOnly)-2:]
        numsOnly = numsOnly[:len(numsOnly)-2]

    for x in range(0, int(len(numsOnly)/3)):
        solution += numsOnly[x * 3:(x*3)+3] + "-"

    solution += endOfNum
    print(solution)
    return solution

def pure_numbers(num):
    numsOnly = ""
    for digit in num:
        if is_number(digit):
            numsOnly += digit

    return numsOnly

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
