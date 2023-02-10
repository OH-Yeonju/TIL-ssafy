T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(N):
            tempV = 0
            for p in range(M):
                for q in range(M):
                    if i+p < N and j+q < N:
                        tempV += lst[i+p][j+q]

            if maxV < tempV:
                maxV = tempV

    print(f'#{tc} {maxV}')