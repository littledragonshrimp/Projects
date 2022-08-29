# new rev avg

import re

hand = open('mbox.txt')
hand = hand.read()

search = re.findall('.*New Revision: ([0-9]+)', hand)
length = len(search)
total = 0

for item in search:
    item = float(item)
    total += item

print(total / length)
