T = int(input())

for tc in range(1, T+1):
    A = list(range(1, 12+1))
    N, K = map(int, input().split())

    cnt = 0
    flst = []
    for i in range(1<<12):
        lst = []
        lstsum = 0
        for j in range(12):
            if i & (1 << j):
                lst.append(A[j])
                lstsum += A[j]

        if len(lst) == N and lstsum == K:
            flst.append(lst)

    print(f'#{tc} {flst}')
