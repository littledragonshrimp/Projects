# recieved email histogram

inp = input('Input file name: ')
try:
    fil = open(inp)
except FileNotFoundError:
    print('Cannot find file try again later.')
    quit()

cum = dict()

for line in fil:
    line = line.rstrip()
    if line.startswith('From') and line.endswith('2008'):
        line = line.split()
        addy = line[1]
        atpos = addy.find('@')
        cum[addy[atpos:]] = cum.get(addy[atpos:], 0) + 1

print(cum)
