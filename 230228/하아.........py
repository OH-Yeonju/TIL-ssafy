for _ in range(4):
    x, y, p, q, x2, y2, p2, q2 = map(int, input().split())
    mx = max(p, p2)
    my = max(q, q2)
    lst = [[0] * (my+1) for _ in range(mx+1)]

    for i in range(x, p+1):
        for j in range(y, q+1):
            lst[i][j] += 1

    for i in range(x2, p2+1):
        for j in range(y2, q2+1):
            lst[i][j] += 2

    res = []
    for i in range(mx+1):
        for j in range(my+1):
            if lst[i][j] == 3:
                res.append((i, j))

    if len(res) == 0:
        print('d')
        continue
    if len(res) == 1:
        print('c')
        continue

    xlst = []
    ylst = []
    for i in res:
        xlst.append(i[0])
        ylst.append(i[1])

    if max(xlst)-min(xlst) >0 and  max(ylst)-min(ylst)>0:
        print('a')
    else:
        print('b')
