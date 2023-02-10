dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flo = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(M):
            sumV = flo[i][j]
            for k in range(4):
                if 0<=i+dr[k]<N and 0<=j+dc[k]<M:
                    sumV += flo[i+dr[k]][j+dc[k]]
            if maxV < sumV:
                maxV = sumV

    print(f'#{tc} {maxV}')