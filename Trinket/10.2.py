# messages per hour of the day

inp = open('mbox-short.txt')

time = dict()

for line in inp:
    line.rstrip()
    if line.startswith('From') and line.endswith('2008'):
        word = line.split()
        colpos = word.find(':')
        hour = word[:colpos + 1]
        time[hour] = time(hour, 0) + 1

print(time.items())
