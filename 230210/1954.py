dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]

    row = 0
    col = 0
    d = 0
    for num in range(1, N*N+1):
        lst[row][col] = num
        newR = row + dr[d]
        newC = col + dc[d]
        if newR < 0 or newR >= N or newC < 0 or newC >= N or lst[newR][newC] != 0:
            d = (d+1)%4
        row += dr[d]
        col += dc[d]

    print(lst)