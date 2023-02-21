def bfs(s):
    Q = []
    visited = [0] * 101
    t = []

    Q.append(s)
    visited[s] = 1
    while Q:
        v = Q.pop(0)
        t.append((v, visited[v]))
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    maxV = 0
    for i in t:
        if i[1] > maxV:
            maxV = i[1]
    maxN = 0
    for i in t:
        if i[1] == maxV and maxN < i[0]:
            maxN = i[0]

    return maxN


for tc in range(1, 10+1):
    D, S = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(100+1)]

    for i in range(0, D, 2):
        v1 = lst[i]
        v2 = lst[i+1]
        G[v1].append(v2)

    print(f'#{tc} {bfs(S)}')