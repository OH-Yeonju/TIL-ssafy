def dfs(v):
    ST = []
    visited = [False] * (V+1)
    road = []

    ST.append(v)
    visited[v] = True

    while ST:
        v = ST.pop()
        road.append(v)
        for w in adjL[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True
    return road

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)

    S, G = map(int, input().split())

    if G in dfs(S):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

