T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전시
    new = [list([0]*N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[i][j] = nums[N-j-1][i]

    new2 = [list([0]*N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new2[i][j] = new[N-j-1][i]

    new3 = [list([0]*N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new3[i][j] = new2[N-j-1][i]

    print(f'#{tc}')
    for _ in range(N):
        print(*new[_], ' ',  *new2[_], ' ',*new3[_], sep='')
