def cnt(num):
    a = 0
    idx = 0
    ct = 0
    m = int(num)
    for i in par[m:]:
        if i == '(':
            a += 1
        if i == ')':
            a -= 1
        if a == 0:
            idx = i

    for i in par[m:idx+1]:
        if i == 0:
            ct += 1

    return ct // 2


T = int(input())

for tc in range(1, T+1):
    f_cnt = 0
    par = list(input())
    N = len(par)

    for i in range(N):
        if par[i] == '(' and par[i+1] == ')':
            par[i] = 0
            par[i+1] = 0


    for i in range(N):
        if par[i] == '(':
            a = cnt(i) + 1
            f_cnt += a
    print(f_cnt)