di = [0, 1, 0, -1] # 오른쪽부터 시계방향
dj = [1, 0, -1, 0]

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(M):
            sumV = s[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += s[ni][nj]
            if maxV < sumV:
                maxV = sumV

    print(f'#{_} {maxV}')