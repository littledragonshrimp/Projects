# number of lines unix

import re

inp = input('Input a regular expression: ')
fil = open('mbox.txt')

count = 0

for line in fil:
    line = line.rstrip()
    exp = re.findall('^recieved', line)
    if len(exp) != 1:
        continue
    count += 1

print(count)
