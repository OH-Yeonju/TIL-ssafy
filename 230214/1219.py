def dfs(v):
    st = []
    visited = [False] * 100

    st.append(v)
    visited[v] = True
    while st:
        v = st.pop()
        if v == 99:
            return 1
        for w in lst[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True
    return 0


for tc in range(1, 10+1):
    T, E = map(int, input().split())
    lst = [[] for _ in range(100)]
    vlst = list(map(int, input().split()))

    for i in range(E):
        v1 = vlst[2*i]
        v2 = vlst[2*i+1]
        lst[v1].append(v2)

    print(f'#{T} {dfs(0)}')