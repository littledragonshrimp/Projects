# number of lines unix

import re

inp = input('Input a regular expression: ')
fil = open('mbox.txt')

count = 0

for line in fil:
    line = line.rstrip()
    exp = re.findall(inp, line)
    if len(exp) != 1:
        continue
    count += 1

print('mbox.txt had', count, 'lines that matched', inp)
