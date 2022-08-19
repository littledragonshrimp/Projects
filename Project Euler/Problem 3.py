# Find the largest prime factor of 600851475143

num = 600851475143
largeprime = None


def compute():
    for x in range(2, num):  # dictates range of number to test
        if num % x == 0:  # tests if the number divisible is a perfect number
            try:
                for y in range(2, x):
                    if x % y == 0:
                        continue
                    else:
                        largeprime = x
            except ValueError:
                continue
    print(largeprime)


print(compute())
