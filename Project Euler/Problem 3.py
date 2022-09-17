# Find the largest prime factor of 600851475143
# UNFINISHED
num = 600851475143
largeprime = None
split = num // 2


def compute():
    for i in reversed(range(split, num)):
        for n in range(2, i // 2):
            if i % n == 0:
                largeprime = i
            else:
                continue
    return largeprime


print(compute())
