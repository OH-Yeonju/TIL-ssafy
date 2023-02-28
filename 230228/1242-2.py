def hextobin(s):
    if s.isdigit():
        decV = int(s)
    else:
        decV = ord(s) - ord('A') + 10
    res = ''
    for j in range(3, -1, -1):
        res += '1' if decV & (1<<j) else '0'
    return res

mapping = {(3, 2, 1, 1):0, (2, 2, 2, 1):1, (2, 1, 2, 2):2,
           (1, 4, 1, 1):3, (1, 1, 3, 2):4, (1, 2, 3, 1):5,
           (1, 1, 1, 4):6, (1, 3, 1, 2):7, (1, 2, 1, 3):8, (3, 1, 1, 2):9}


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    sec = []
    for i in lst:
        if i not in sec:
            sec.append(i)

    num = []
    for i in sec:
        tmp = ''
        for j in i:
            tmp += str(hextobin(j))
        num.append(tmp)

    lst = []
    n = []
    for i in num:
        cnt = 0
        for j in range(len(i)):


    print(n)
