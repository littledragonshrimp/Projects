# Largest palindrome product
largestvalue = None
largestdiv = None
palindromes = list()

for i in range(10, 998001):
    if i == (int(str(i)[::-1])):  # all palindromes to list
        palindromes.append(i)

for n in palindromes:
    for i in range(100, 999):
        if n % i == 0 and (len(str(n / i))) == 3:
            largestvalue = n
            largestdiv = i
            break
        else:
            continue


print(largestvalue, largestdiv)
