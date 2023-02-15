dr = [0, 1, 0, -1, -1, 1, 1, -1]
dc = [1, 0, -1, 0, 0, 1, -1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    othello = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N//2, N//2+2):
        for j in range(N//2, N//2+2):
            if i == j:
                othello[i][j] = 2
            else:
                othello[i][j] = 1


    for _ in range(M):
        row, col, color = map(int, input().split())
        othello[row][col] = color

        d = 0
        if color == 1:
            for i in range(8):
                newR = row + dr[d] * i
                newC = col + dc[d] * i
                if 1<=newR<N+1 and 1<=newC<N+1:
                    if othello[newR][newC] == 1:
                        if row == newR:
                            if col > newC:
                                for j in range(newC, col):
                                    othello[row][j] = 1
                            else:
                                for j in range(col, newC):
                                    othello[row][j] = 1
                        elif col == newC:
                            if row > newR:
                                for j in range(newR, row):
                                    othello[j][col] = 1
                            else:
                                for j in range(row, newR):
                                    othello[j][col] = 1
                        elif


    print(othello)
