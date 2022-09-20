def numberOfSteps(num):
    count = 0
    while num != 0:
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
    return count


print(numberOfSteps(123))
