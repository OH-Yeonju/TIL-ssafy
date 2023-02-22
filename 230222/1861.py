# def bfs(row, col, m):
#     Q = []
#     Q.append((row, col))
#
#     while Q:
#         r, c = Q.pop(0)
#         for i in range(4):
#             newR = r + dr[i]
#             newC = c + dc[i]
#             if 0<=newR<N and 0<=newC<N and lst[newR][newC] == lst[r][c] + 1:
#                 Q.append((newR, newC))
#                 m += 1
#     return (lst[row][col], m)
#
#
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    move = 0
    minN = 1000000

    for i in range(N):
        for j in range(N):
            Q = []
            visited = 0
            Q.append((i, j, visited))
            while Q:
                r, c, mo = Q.pop(0)
                for i in range(4):
                    newR = r + dr[i]
                    newC = c + dc[i]
                    if 0<=newR<N and 0<=newC<N and lst[newR][newC]- lst[r][c] == 1:
                        Q.append((newR, newC, mo+1))
            if move < visited:
                move = visited


    print(visited)








# move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#
# T = int(input())
# for case in range(1, T + 1):
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#     room_min = 0
#     go = 0
#
#     for i in range(N):
#         for j in range(N):
#             visited = 0
#             queue = [[i, j, 0]]
#             while queue:
#                 y, x, temp = queue.pop(0)  # visited >> 횟수
#                 visited = max(temp, visited)
#                 for dy, dx in move:
#                     ny, nx = y + dy, x + dx
#                     # 범위를 넘지않고, 방의차가 1일 때
#                     if 0 <= ny < N and 0 <= nx < N and room[ny][nx] - room[y][x] == 1:
#                         queue.append([ny, nx, visited + 1])
#             if go < visited:  # 방문거리 최대 찾기
#                 go = visited
#                 room_min = room[i][j]
#             elif go == visited:
#                 if room_min > room[i][j]:
#                     room_min = room[i][j]
#     print(f'#{case} {room_min} {go + 1}')