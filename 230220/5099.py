T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    for i in range(M):
        C[i] = [i+1, C[i]]

    Q = C[:N]
    p = C[N:]

    while len(Q) != 1:
        q = Q.pop(0)
        q[1] = q[1] // 2
        if q[1] == 0:
            if p:
                Q.append(p.pop(0))
        else:
            Q.append(q)

    print(f'#{tc} {Q[0][0]}')
