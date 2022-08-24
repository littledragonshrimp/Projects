# 10,001st prime #

import math


def compute():
    count = 0
    lastprime = None
    n = 2
    while count != 10001:
        a = prime(n)
        if a != -1:
            count += 1
            lastprime = n
            n += 1
        else:
            continue
    return str(lastprime)


def prime(n):
    uprange = math.isqrt(n + 1)
    for i in range(2, uprange):
        if n % i == 0:
            return (-1)

        else:
            return int(n)


print(compute())
