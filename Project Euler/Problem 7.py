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
<<<<<<< HEAD
    for i in range(2, math.isqrt(n) + 1):
=======
    uprange = math.isqrt(n + 1)
    for i in range(2, uprange):
>>>>>>> b48540604e858b759b3c2236e4c87e7c891b57a0
        if n % i == 0:
            return (-1)

        else:
            return int(n)


print(compute())
