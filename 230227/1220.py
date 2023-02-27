for tc in range(1, 10+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for j in range(100):
        ST = []
        for i in range(100):
            if not ST and lst[i][j] == 1:
                ST.append(1)
            if ST and lst[i][j] == 2:
                ST.pop()
                cnt += 1

    print(f'#{tc} {cnt}')