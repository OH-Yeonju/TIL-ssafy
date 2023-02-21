def bfs(row, col):
    Q = []
    visited = [[0] * N for _ in range(N)]

    Q.append((row, col))
    visited[row][col] = 1

    while Q:
        r, c = Q.pop(0)
        for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            newR = r + dr
            newC = c + dc
            if 0<=newR<N and 0<=newC<N and lst[newR][newC] != 1 and not visited[newR][newC]:
                visited[newR][newC] = visited[r][c] + 1
                if lst[newR][newC] == 3:
                    return visited[newR][newC]-2
                Q.append((newR, newC))
    return 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]

    row = 0
    col = 0
    row2 = 0
    col2 = 0
    for i in range(len(lst)):
        if 2 in lst[i]:
            row = i
            col = lst[i].index(2)

    for i in range(len(lst)):
        if 3 in lst[i]:
            row2 = i
            col2 = lst[i].index(3)

    print(f'#{tc} {bfs(row, col)}')
