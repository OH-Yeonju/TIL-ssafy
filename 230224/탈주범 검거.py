p = [[],[0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
opp = {0:1, 1:0, 2:3, 3:2}
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(si, sj, L):
    q = []
    v = [[0]*M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return cnt
        # 파이프에 연결된 방향 처리
        for dr in p[arr[ci][cj]]:
            ni, nj = ci+di[dr], cj+dj[dr]
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and opp[dr] in p[arr[ni][nj]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1
                cnt += 1
    return cnt




T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(R, C, L)

    print(f'#{tc} {ans}')