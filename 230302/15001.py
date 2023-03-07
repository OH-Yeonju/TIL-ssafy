T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]

    s = N//2
    e = N//2
    sumV = 0
    for i in range(N):
        for j in range(s, e+1):
            sumV += lst[i][j]

        if i < N//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {sumV}')
