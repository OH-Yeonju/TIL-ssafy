T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    minV = 2500
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for a in range(0, i+1):
                for k in range(M):
                    if lst[a][k] != 'W':
                        cnt += 1
            for b in range(i+1, j+1):
                for k in range(M):
                    if lst[b][k] != 'B':
                        cnt += 1
            for c in range(j+1, N):
                for k in range(M):
                    if lst[c][k] != 'R':
                        cnt += 1
            if cnt < minV:
                minV = cnt
    print(f'#{tc} {minV}')