T = int(input())

for tc in range(1, T+1):
    N = int(input())
    full = [[0] * 10 for _ in range(9+1)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                full[j][k] += color

        cnt = 0

        for i in range(10):
            for j in range(10):
                if full[i][j] == 3:
                    cnt += 1

    print(f'#{tc} {cnt}')