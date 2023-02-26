T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = [0] * (N+1)
    for _ in range(M):
        n1, n2 = map(int, input().split())
        lst[n1] = n2

    for i in range(N, 0, -1):
        if i // 2 > 0:
            lst[i//2] = lst[i//2] + lst[i]

    print(f'#{tc} {lst[L]}')
