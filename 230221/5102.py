def bfs(s):
    visited = [0] * (V+1)
    Q = []
    Q.append(s)
    visited[s] = 1

    while Q:
        v = Q.pop(0)
        for w in lst[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v]+1

    if visited[G] == 0:
        return 0
    return visited[G]-1



T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range((V+1))]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        lst[v1].append(v2)
        lst[v2].append(v1)
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S)}')