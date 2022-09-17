n = int(600851475143 / 71)
# print(n / 71)
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        quit()
