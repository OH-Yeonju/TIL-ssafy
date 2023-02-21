def dfs(row, col):
    Q = []
    visited = [[0]*16 for _ in range(16)]

    Q.append((row, col))
    visited[row][col] = 1

    while Q:
        r, c = Q.pop(0)
        for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            newR = r + dr
            newC = c + dc
            if 0<=newR<16 and 0<=newC<16 and lst[newR][newC] != 1 and not visited[newR][newC]:
                visited[newR][newC] = visited[r][c] + 1
                if lst[newR][newC] == 3:
                    return 1
                Q.append((newR, newC))

    return 0


for _ in range(10):
    tc = int(input())
    lst = [list(map(int, input())) for _ in range(16)]
    print(f'#{tc} {dfs(1, 1)}')