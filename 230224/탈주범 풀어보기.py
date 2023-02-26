pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
opp = {0:1, 1:0, 2:3, 3:2}

def bfs(r, c, l):
    Q = []
    visited = [[0]*M for _ in range(N)]

    Q.append((r, c))
    visited[r][c] = 1
    cnt = 1

    while Q:
        row, col = Q.pop(0)
        if visited[row][col] == l:
            return cnt

        for d in pipe[lst[row][col]]:
            newR = row + dr[d]
            newC = col + dc[d]
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC] and opp[d] in pipe[lst[newR][newC]]:
                Q.append((newR, newC))
                visited[newR][newC] = visited[row][col] + 1
                cnt += 1
    return cnt


T = int(input())

for tc in range(1,T+1):
    N,M,R,C,L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    print(f'{tc} {bfs(R, C, L)}')
