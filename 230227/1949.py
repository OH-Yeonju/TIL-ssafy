dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

def per(row, col):
    ST = []
    visited = [[0]*N for _ in range(N)]
    ST.append((row, col))
    visited[row][col] = 1

    while ST:
        r, c = ST.pop()
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0<=newR<N and 0<=newC<N and not visited[newR][newC]:
                visited[newR][newC] = visited[r][c] + 1






T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            per(i, j)