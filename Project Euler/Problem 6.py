# difference of sqr of sum and sum of sqr


def compute():
    x = 0
    y = 0
    for i in range(1, 101):
        x += i
        y += i ** 2
    ans = (x ** 2) - y
    return str(ans)


print(compute())
