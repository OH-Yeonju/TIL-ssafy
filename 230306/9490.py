dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N):
        for j in range(M):
            cnt = lst[i][j]
            for k in range(4):
                for p in range(1, lst[i][j]+1):
                    newR = i + dr[k]*p
                    newC = j + dc[k]*p
                    if 0<=newR<N and 0<=newC<M:
                        cnt += lst[newR][newC]
            if cnt > maxV:
                maxV = cnt
    print(f'#{tc} {maxV}')