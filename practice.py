# returns min and max

numlist = list()
inp = None

while inp != 'done':
    inp = input('Input a number: ')
    try:
        if inp == 'done':
            continue
        else:
            num = int(inp)
            numlist.append(num)
    except TypeError:
        print('Please input a number or "done".')
        continue

print(max(numlist), 'is the max.', min(numlist), 'is the min')
