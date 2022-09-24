nums = [2, 7, 3]
target = 9


def solution():
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            if nums[a] + nums[b] == target:
                return [a, b]


print(solution())
