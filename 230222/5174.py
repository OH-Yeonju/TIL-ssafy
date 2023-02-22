def findA(N):
    global cnt
    if leftC[N] != 0:
        cnt += 1
        findA(leftC[N])
    if rightC[N] != 0:
        cnt += 1
        findA(rightC[N])
    return cnt


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    leftC = [0] * (E+2)
    rightC = [0] * (E+2)
    parent = [0] * (E+2)
    cnt = 0

    for i in range(E):
        p = lst[2*i]
        c = lst[2*i+1]
        parent[c] = p
        if leftC[p] == 0:
            leftC[p] = c
        else:
            rightC[p] = c

    findA(N)
    print(f'#{tc} {cnt+1}')