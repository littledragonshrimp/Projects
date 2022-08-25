# read and add words to dict

fil = open('words.txt')
wordfile = fil.read()
words = dict()
n = 1

for word in wordfile.split():
    words[word] = n
    n += 1

print('real' in words)
