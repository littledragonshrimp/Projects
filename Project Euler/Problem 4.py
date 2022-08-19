# Largest palindrome product
import math


for i in reversed(range(0, 998001)):
    if i == reversed(str(i)):  # If it is palindrome number
        for s in reversed(range(math.sqrt(i)-100, math.sqrt(i))):
            if i % s == 0:
                print(i)
                quit()
            else:
                continue
    else:
        continue
