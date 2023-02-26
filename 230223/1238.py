def bfs(s):
    Q = []
    visited = [0] * 101

    Q.append(s)
    visited[s] = 1
    while Q:
        s = Q.pop(0)
        for w in G[s]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[s] + 1
    maxV = 0
    maxIdx = 0
    for i in range(len(visited)):
        if visited[i] >= maxV:
            maxV = visited[i]
            maxIdx = i
    return maxIdx


for tc in range(1, 10+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [[] for _ in range(101)]

    for i in range(N//2):
        n1 = lst[2*i]
        n2 = lst[2*i+1]
        G[n1].append(n2)
    print(f'#{tc} {bfs(S)}')