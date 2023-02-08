T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(N)]

    f_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if num_lst[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    f_cnt += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            f_cnt += 1

    for i in range(N):
        cnt = 0
        for j in range(N):
            if num_lst[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    f_cnt += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            f_cnt += 1

    print(f'#{tc} {f_cnt}')

