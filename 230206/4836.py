T = int(input())

for tc in range(1, T+1):
    n = int(input())
    c1_lst = []
    c2_lst = []
    cnt = 0
    for nc in range(n):
        c_lst = list(map(int, input().split()))
        if c_lst[4] == 1:
            for i in range(c_lst[0], c_lst[2]+1):
                for j in range(c_lst[1], c_lst[3]+1):
                    c1_lst.append([i, j])

        else:
            for i in range(c_lst[0], c_lst[2]+1):
                for j in range(c_lst[1], c_lst[3]+1):
                    c2_lst.append([i, j])
    for i in c1_lst:
        if i in c2_lst:
            cnt += 1
    print(f'#{tc} {cnt}')