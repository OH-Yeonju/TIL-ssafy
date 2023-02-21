# def BFS(G, v):
#     visited = 0*(n+1)  # n: 정점의 개수
#     queue = []
#     queue.append(v)
#     visited[v] = 1
#     while queue:
#         t = queue.pop(0)
#         visit(t)
#         for i in G[t]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = visited[n]+1  # 방문순서표시됨... 중간에 거쳐가는 길의 개수 알수있음


'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v, N):  # 시작점, 마지막 정점 번호
    visited = [0] * (N+1) # visited 생성
    q = [v]               # 큐 생성
    visited[v] = 1        # 시작점 인큐 표시
    while q:              # 큐가 비어있지 않으면
        t = q.pop(0)                # 디큐
        print(t, end=' ')           # T에서 처리할 일
        for v in adjL[t]:           # t에 인접이고 방문한 적 없는 v
            if visited[v] == 0:
                q.append(v)         # v 인큐
                visited[v] = visited[t]+1  # v 인큐되었음 표시
    print()
    print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1, V)   # 시작정점 1, 마지막 정점 V