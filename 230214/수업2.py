V = 7 + 1  # (0번은 안씀)
S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
S = list(map(int, S.split()))


# 인접 행렬 만들기
G = [[0] * V for _ in range(V)]
for idx in range(0, len(S), 2):
    v1 = S[idx]
    v2 = S[idx + 1]
    G[v1][v2] = 1
    G[v2][v1] = 1

# 인접 리스트 만들기
G = [[] for _ in range(V)]

for idx in range(0, len(S), 2):
    v1 = S[idx]
    v2 = S[idx+1]
    G[v1].append(v2)  # 만약 화살표가 있다면 방향에 맞게만 넣어줘야
    G[v2].append(v1)

print(G)


G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]

# 재귀로
visited = [False] * V
def dfsr(v):
    print(v)
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfsr(w)

# 더 간단하게
def dfs(v):
    ST = []
    visited = [False] * V

    ST.append(v)
    visited[v] = True
    while ST:
        v = ST.pop()
        print(v)
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True



# 간단하게
def dfs(v):
    ST = []
    visited = [False] * V

    ST.append(v)
    while ST:
        v = ST.pop()
        if not visited[v]:
            visited[v] = True
            print(v)
        for w in G[v]:
            if not visited[w]:
                ST.append(w)


# 순서대로
def dfs(v):
    ST = []
    visited = [False] * V  # 방문 표시 넣어줄 곳

    ST.append(v)
    visited[v] = True
    print(v)
    while ST:  #len(ST) > 0:
        for w in G[v]:
            if not visited[w]:  # w가 안 간 길이면
                visited[w] = True   # 간다
                print(w)
                ST.append(v)   # 지나온 길 저장
                v = w    # 여기서 다시 시작
                break
        else:  # 다 돌았는데 길이 안나왔으면
            v = ST.pop()


dfs(1)
dfsr(1)

# 인접행렬으로
def dfs(v):
    ST = []
    visited = [False] * V

    ST.append(v)
    visited[v] = True
    while ST:
        v = ST.pop()
        print(v)
        for w in range(V):
            if G[v][w] and not visited[w]:
                ST.append(w)
                visited[w] = True