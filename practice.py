import math


def compute():
    n = 600851475143
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return str(n)


def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return i
    return n  # n itself is prime


print(compute())
