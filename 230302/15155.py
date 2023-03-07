dr = [1, 1]
dc = [1, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [input() for _ in range(N)]
    fcnt = 0

    # 가로보기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if lst[i][j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    fcnt += 1
                cnt = 0
        if cnt >= 5:
            fcnt += 1

    # 세로보기
    for j in range(N):
        cnt = 0
        for i in range(N):
            if lst[i][j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    fcnt += 1
                cnt = 0
        if cnt >= 5:
            fcnt += 1

    # 대각선보기
    d = 0
    for i in range(N):
        if lst[0][i] == 'o':
            newR = 0+dr[d]
            newC = i+dc[d]
            cnt1 = 0
            while 0<=newR<N and 0<=newC<N:
                if lst[newR][newC] == 'o':
                    cnt1 += 1
                else:
                    if cnt1 >= 5:
                        fcnt += 1
                    cnt1 = 0
                newR = newR + dr[d]
                newC = newC + dr[d]
            if cnt1 >= 5:
                fcnt += 1

        if lst[i][0] == 'o':
            newR = i+dr[d]
            newC = 0+dc[d]
            cnt1 = 0
            while 0<=newR<N and 0<=newC<N:
                if lst[newR][newC] == 'o':
                    cnt1 += 1
                else:
                    if cnt1 >= 5:
                        fcnt += 1
                    cnt1 = 0
                newR = newR + dr[d]
                newC = newC + dr[d]

            if cnt1 >= 5:
                fcnt += 1

    d = 1
    for i in range(N):
        if lst[0][i] == 'o':
            newR = 0 + dr[d]
            newC = i + dc[d]
            cnt1 = 0
            while 0 <= newR < N and 0 <= newC < N:
                if lst[newR][newC] == 'o':
                    cnt1 += 1
                else:
                    if cnt1 >= 5:
                        fcnt += 1
                    cnt1 = 0
                newR = newR + dr[d]
                newC = newC + dr[d]
            if cnt1 >= 5:
                fcnt += 1

        if lst[i][N-1] == 'o':
            newR = i + dr[d]
            newC = N-1 + dr[d]
            cnt1 = 0
            while 0 <= newR < N and 0 <= newC < N:
                if lst[newR][newC] == 'o':
                    cnt1 += 1
                else:
                    if cnt1 >= 5:
                        fcnt += 1
                    cnt1 = 0
                newR = newR + dr[d]
                newC = newC + dr[d]

            if cnt1 >= 5:
                fcnt += 1



    if fcnt > 0:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
