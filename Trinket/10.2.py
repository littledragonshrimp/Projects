# messages per hour of the day

inp = open('mbox-short.txt')

hist = dict()
lhist = list()

for line in inp:
    line = line.rstrip()
    if line.startswith('From') and line.endswith('2008'):
        word = line.split()
        time = word[5]
        hour = time[:2]
        hist[hour] = hist.get(hour, 0) + 1

for key, value in hist.items():
    lhist.append((key, value))

lhist.sort()

for items in lhist:
    print(items)
