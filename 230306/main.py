T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    minV = 2500             # N*M 최대값
    for a in range(N-2):    # W영역 맨 아래 0~N-3
        for b in range(a+1, N-1):  # B영역 맨 아래 a+1~N-2
            cnt = 0         # 각 영역에서 새로 칠하는 횟수
            for i in range(0, a+1):
                for j in range(M):
                    if arr[i][j] != 'W':
                        cnt += 1
            for i in range(a+1, b+1):
                for j in range(M):
                    if arr[i][j] != 'B':
                        cnt += 1
            for i in range(b+1, N):
                for j in range(M):
                    if arr[i][j] != 'R':
                        cnt += 1
            if minV > cnt:
                minV = cnt
    print(f'#{tc} {minV}')

