def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rndict = dict()
    mgdict = dict()
    for a in ransomNote:
        rndict[a] = rndict.get(a, 0) + 1
    for a in magazine:
        mgdict[a] = mgdict.get(a, 0) + 1

    compare = {k: mgdict[k]
               for k in mgdict
               if k in rndict and mgdict[k] >= rndict[k]}
    if len(compare) == len(rndict):
        return True
    else:
        False
