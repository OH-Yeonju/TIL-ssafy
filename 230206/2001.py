T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(N):
            sumV = 0
            for k in range(M):
                for p in range(M):
                    if 0 <= i+k < N and 0 <= j+p < N:
                        sumV += s[i+k][j+p]
            if sumV > maxV:
                maxV = sumV
    print(f'#{tc} {maxV}')
