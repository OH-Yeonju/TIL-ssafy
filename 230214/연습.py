dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(H)]


    # 깼을때 합 구하기.. 동시에깨진다면..?
    for i in range(H):
        for j in range(W):
            numsum = lst[i][j]
            if lst[i][j] > 0 and lst[i-1][j] == 0:
                if lst[i][j] == 1:
                    lst[i][j] == 0
                else:
                    for p in range(1, lst[i][j]):
                        for k in range(4):
                            lst[i+dr[k]*p][j+dc[k]*p]





