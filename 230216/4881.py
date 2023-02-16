def per(k, curS):
    global minsum
    if curS > minsum:
        return
    if k==N:
        if curS < minsum:
            minsum = curS
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            a[k] = lst[k][i]
            per(k+1, curS + lst[k][i])
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # nlst = [[0] * N for _ in range(N)]
    #
    # for j in range(N):
    #     for i in range(N):
    #         nlst[i][j] = lst[j][i]
    # print(nlst)
    a = [-1] * N
    visited = [False] * N
    minsum = 9999
    per(0, 0)
    print(f'#{tc} {minsum}')


    # def per(k):
    #     if k == N:
    #         global minsum
    #         sum = 0
    #         for i in a:
    #             sum += i
    #         if sum < minsum:
    #             minsum = sum
    #         return
    #
    #     for i in range(N):
    #         if not visited[i]:
    #             visited[i] = True
    #             a[k] = lst[k][i]
    #             per(k + 1)
    #             visited[i] = False
    #
    #
    # T = int(input())
    #
    # for tc in range(1, T + 1):
    #     N = int(input())
    #     lst = [list(map(int, input().split())) for _ in range(N)]
    #     # nlst = [[0] * N for _ in range(N)]
    #     #
    #     # for j in range(N):
    #     #     for i in range(N):
    #     #         nlst[i][j] = lst[j][i]
    #     # print(nlst)
    #     a = [-1] * N
    #     visited = [False] * N
    #     minsum = 9999
    #     per(0)
    #     print(f'#{tc} {minsum}')
