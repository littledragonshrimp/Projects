accounts = [[3, 3], [3, 7], [2, 7]]


def maximumWealth():
    wealth = 0
    for i in range(len(accounts)):
        total = sum(accounts[i - 1])
        if int(total) > wealth:
            wealth = total
        else:
            continue
    return wealth


print(maximumWealth())
