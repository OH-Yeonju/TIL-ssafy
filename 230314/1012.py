def bfs(row, col):
    Q = []
    visited = [[0] * M for _ in range(N)]

    Q.append((row, col))
    visited[row][col] = 1

    while Q:
        r, c = Q.pop(0)
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newR = r + dr
            newC = c + dc
            if 0<=newR<N and 0<=newC<M and lst[newR][newC] == 0 and visited[newR][newC] == 0:
                visited[newR][newC] = visited[r][c] + 1
                Q.append((newR, newC))

    return visited




M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
flst = []
visited = [[0]*M for _ in range(N)]
fv = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            flst.append((i, j))

for i in flst:
    row, col = i
    v = bfs(row, col)
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                visited[i][j] = v[i][j]
            else:
                if visited[i][j] > v[i][j]:
                    visited[i][j] = v[i][j]

print(visited)