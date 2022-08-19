# Sum of even fibonacci numbers

fin = 2
term = 0  # next term in fibonacci sequence
t1 = 1  # first term in finobacci sequence
t2 = 2  # second term

while term <= 4000000:
    term = t1 + t2
    t1 = t2
    t2 = term
    if t2 % 2 == 0:
        fin += t2

print(fin)
