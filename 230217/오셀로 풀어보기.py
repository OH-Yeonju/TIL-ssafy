dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)]
    n = N//2
    arr[n][n] = arr[n+1][n+1] = 2
    arr[n][n+1] = arr[n+1][n] = 1

    for _ in range(M):
        row, col, color = map(int, input().split())

        for i in range(8):
            lst = []
            for mul in range(1, N):
                nr = row + dr[i] * mul
                nc = col + dc[i] * mul
                arr[row][col] = color
                if arr[nr][nc] == 0:
                    break
                elif arr[nr][nc] != color:
                    lst.append((nr, nc))
                else:
                    for j in lst:
                        ni, nj = j
                        arr[ni][nj] = color
                    break
        b = 0
        w = 0
        for i in range(N+2):
            for j in range(N+2):
                if arr[i][j] == 1:
                    b += 1
                if arr[i][j] == 2:
                    w += 1

    print(f'#{tc} {b} {w}')