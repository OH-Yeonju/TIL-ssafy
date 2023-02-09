T = 'This pattern matching algorithms'

def bmoor(P):
    lenP = len(P)
    lenT = len(T)
    SKIP = [lenP] * 128
    for i in range(lenP-1):
        t = P[i]
        SKIP[ord(t)] = lenP-1-i
    # print(SKIP[ord('p')])

    idxT = 0
    while idxT+lenP <= lenT:
        idxP = lenP-1
        while idxP >= 0 and T[idxT+idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1:
            return idxT
        # ascii = ord(T[idxT+idxP])
        # j = SKIP[ascii]
        idxT += SKIP[ord(T[idxT + idxP])]

    return -1



def brute(P):
    lenP = len(P)
    lenT = len(T)
    for idxT in range(0, lenT - lenP+1):
        # for idxP in range(lenP):
        #     if T[idxT] == P[idxP]:
        #         continue
        #     else:
        #         break
        idxP = 0
        while idxP < lenP and T[idxT+idxP] == P[idxP]:
            idxP += 1
        if idxP == lenP:
            return idxT
    return -1 # 다 돌았는데 못찾았을경우


print(bmoor('pat'))
# print(T.find('patt'))