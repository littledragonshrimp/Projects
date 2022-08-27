# letter frequency

fil = open('mbox-short.txt')

string = fil.read().lower()

let_hist = dict()
ll_hist = list()

for char in string:
    if char.isalpha():
        let_hist[char] = let_hist.get(char, 0) + 1

for key, value in let_hist.items():
    ll_hist.append((key, value))

ll_hist.sort()

for items in ll_hist:
    print(items)
