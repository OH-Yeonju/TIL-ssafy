T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    maxlen = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if lst[i][j] == 1:
                cnt += 1
                if maxlen < cnt:
                    maxlen = cnt
            else:
                cnt = 0

    for j in range(M):
        cnt = 0
        for i in range(N):
            if lst[i][j] == 1:
                cnt += 1
                if maxlen < cnt:
                    maxlen = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxlen}')