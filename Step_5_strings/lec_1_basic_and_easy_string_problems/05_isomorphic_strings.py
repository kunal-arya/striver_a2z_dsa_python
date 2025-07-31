

def isIsomorphic(s: str, t: str) -> bool:
    n = len(s)
    hashST = {}
    hashTS = {}

    for c1, c2 in zip(s,t):
        if((c1 in hashST and hashST[c1] != c2) or (c2 in hashTS and hashTS[c2] != c1)):
            return False

        hashST[c1] = c2
        hashTS[c2] = c1

    return True

print(isIsomorphic(s= "badc", t= "baba"))