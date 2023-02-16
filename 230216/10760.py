dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    d = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            mcnt = 0
            for k in range(8):
                newR = i + dr[k]
                newC = j + dc[k]
                if 0<=newR<N and 0<=newC<M and lst[newR][newC] < lst[i][j]:
                    mcnt += 1
            if mcnt >= 4:
                cnt += 1

    print(f'#{tc} {cnt}')