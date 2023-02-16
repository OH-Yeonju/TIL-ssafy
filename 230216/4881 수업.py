def per(k, curS):
    global minV
    if minV < curS:
        return
    if k==N:
        # # print(bits)
        # sumV = 0
        # for i in range(N):
        #     # col = bits[i]
        #     # row = i
        #     sumV += ARR[i][bits[i]]
        # # print(sumV)
        # if minV > sumV:
        #     minV = sumV
        if minV > curS:
            minV = curS
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            bits[k] = i
            per(k+1, curS+ARR[k][i])
            visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    minV = 100
    bits = [-1] * N
    visited = [False] * N
    per(0, 0)
    print(minV)