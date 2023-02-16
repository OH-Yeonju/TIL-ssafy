def game(l, r):
    if l==r:
        return r

    m = (l+r)//2
    lwinner = game(l, m)
    rwinner = game(m+1, r)

    return cal(lwinner, rwinner)