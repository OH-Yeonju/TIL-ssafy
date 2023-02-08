T = int(input())
for tc in range(1, T + 1):
    N = int(input())

# 방향전환(오른, 아래, 왼, 위 순)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ARR = [[0]*N for _ in range(N)]
    row = 0
    col = 0
    d = 0
    for i in range(1, N*N+1):
        ARR[row][col] = i
        newR = row + dr[d]
        newC = col + dc[d]
        if newR<0 or newR>=N or newC<0 or newC>=N or ARR[row + dr[d]][col + dc[d]] != 0:
            d = (d+1) % 4

        row = row + dr[d]
        col = col + dc[d]

    print(f'#{tc}')
    for i in ARR:
        print(*i)