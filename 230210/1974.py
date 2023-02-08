T = int(input())

for tc in range(1, T + 1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    ro = 0

    # 가로보기
    for i in range(9):
        n = []
        for j in range(9):
            if sdoku[i][j] in n:
                ro += 1
            else:
                n.append(sdoku[i][j])

    # 세로보기
    for j in range(9):
        m = []
        for i in range(9):
            if sdoku[i][j] in m:
                ro += 1
            else:
                m.append(sdoku[i][j])


    # 사각형보기
    n_lst = [0, 3, 6]

    for i in n_lst:
        for j in n_lst:
            v = []
            for p in range(3):
                for q in range(3):
                    if sdoku[i+p][j+q] in v:
                        ro += 1
                    else:
                        v.append(sdoku[i+p][j+q])
    if ro!=0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')




