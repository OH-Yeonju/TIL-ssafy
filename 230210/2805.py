T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    mi = N//2
    col_l = N//2
    col_r = N//2
    allsum = 0

    for i in range(N):
        for j in range(col_l, col_r+1):
            allsum += farm[i][j]
        if i < mi:
            col_l -= 1
            col_r += 1
        else:
            col_l += 1
            col_r -= 1

    print(f'#{tc} {allsum}')