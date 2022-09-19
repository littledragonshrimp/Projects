nums = [1, 2, 3, 4]


def compute():
    count = 0
    sums = list()
    for i in range(len(nums)):
        count += 1
        sums.append(sum(nums[:count]))
    return sums


print(compute())
