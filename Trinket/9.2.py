# parse and index

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
        cum[line[2]] = cum.get(line[2], 0) + 1

print(cum)
