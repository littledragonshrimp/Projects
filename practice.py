ransom = "abc"
mag = "abcd"


def solution():
    if len(ransom) > len(mag):
        return False
        quit()
    ransomdict = dict()
    magdict = dict()
    for i in ransom:
        ransomdict[i] = ransomdict.get(i, 0) + 1
    for i in mag:
        magdict[i] = magdict.get(i, 0) + 1
    print(ransomdict, magdict)
    if ransomdict == magdict:
        print("True")


solution()
