nums = [1, 2, 3, 4]


def runningSum():
    res = [nums[0]] + [0] * (len(nums) - 1)
    return res
    for i, num in enumerate(nums[1:]):
        res[i + 1] += res[i] + num
    return res


print(runningSum())
