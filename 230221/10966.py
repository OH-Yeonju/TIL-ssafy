from collections import deque

# def bfs(row, col):
#     Q = []
#     visited = [[0] * M for _ in range(N)]
#
#     Q.append((row, col))
#     visited[row][col] = 1
#
#     while Q:
#         r, c = Q.pop(0)
#         for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
#             newR = r + dr
#             newC = c + dc
#             if 0<=newR<N and 0<=newC<M and not visited[newR][newC]:
#                 visited[newR][newC] = visited[r][c] + 1
#                 if lst[newR][newC] == 'W':
#                     return visited[newR][newC]
#                 Q.append((newR, newC))
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     lst = [list(map(str, input())) for _ in range(N)]
#     cnt = 0
#     lcnt = 0
#     Q = deque()
#     visited = [[999999999] * M for _ in range(N)]
#
#     for i in range(N):
#         for j in range(M):
#             if lst[i][j] == 'W':
#                 Q.append((i, j))
#                 visited[i][j] = 1
#                 while Q:
#                     r, c = Q.popleft()
#                     for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
#                         newR = r + dr
#                         newC = c + dc
#                         if 0<=newR<N and 0<=newC<M and lst[newR][newC] == 'L' and not visited[newR][newC]:
#                             if visited[newR][newC] != 0 and visited[newR][newC] >= visited[r][c]+1:
#                                 visited[newR][newC] = visited[r][c] + 1
#                             else:
#                                 break
#
#                             Q.append((newR, newC))
#
#
#     for i in range(N):
#         for j in range(M):
#             if lst[i][j]== 'L':
#                 cnt += visited[i][j]
#
#     print(visited)



    # print(f'#{tc} {cnt}')




# def bfs(row, col):
#     Q = []
#     visited = [[0] * M for _ in range(N)]
#
#     Q.append((row, col))
#     visited[row][col] = 1
#
#     while Q:
#         r, c = Q.pop(0)
#         for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
#             newR = r + dr
#             newC = c + dc
#             if 0<=newR<N and 0<=newC<M and not visited[newR][newC]:
#                 visited[newR][newC] = visited[r][c] + 1
#                 if lst[newR][newC] == 'W':
#                     return visited[newR][newC]
#                 Q.append((newR, newC))



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    Q = deque()
    cnt = 0
    lcnt = 0

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'L':
                lcnt += 1
                Q.append((i, j))
                visited[i][j] = 1
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            newR = r + dr
            newC = c + dc
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC]:
                if visited[newR][newC] != 0 and lst[newR][newC]
                visited[newR][newC] = visited[r][c] + 1
                # if lst[newR][newC] == 'W':
                #     cnt += visited[newR][newC]
                #     continue
                Q.append((newR, newC))

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'L':
                cnt += visited[i][j]

    print(visited)
    # print(f'#{tc} {cnt}')