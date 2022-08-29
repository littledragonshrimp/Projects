import re

hand = open('mbox.txt')
hand = hand.read().rstrip()
exp = re.findall('^X-', hand)
print(exp)
