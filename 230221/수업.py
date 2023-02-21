from collections import deque



def bfs(s):
    # Q = []
    Q = deque()
    # visited = [False] * (N+1)
    visited = [0] * (N+1)

    Q.append(s)
    visited[s] = 1
    while Q:
        # v = Q.pop(0)
        v = Q.popleft()
        print(v, visited[v])
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v]+1
    # return visited

def dfs(s):
    ST = []
    visited = [False] * (N+1)

    ST.append(s)
    visited[s] = True
    while ST:
        v = ST.pop(-1)
        print(v)

        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True





N = 7
s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'

lst = list(map(int, s.split()))
G = [[] for _ in range(N+1)]
for idx in range(0, len(lst), 2):
    p1 = lst[idx]
    p2 = lst[idx+1]
    G[p1].append(p2)
    G[p2].append(p1)
print(G)

# bfs(3)  #시작지점
dfs(1)