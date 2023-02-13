T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pa = []
    for i in range(N):
        lst = []
        if i == 0:
            lst.append(1)
        if i >= 1:
            for j in range(i+1):
                if 0 < j < i:
                    lst.append(pa[i-1][j-1] + pa[i-1][j])
                elif j == 0:
                    lst.append(1)
                elif j == i:
                    lst.append(1)
        pa.append(lst)
    print(f'#{tc}')
    for i in pa:
        print(*i)
