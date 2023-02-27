T = int(input())

for tc in range(1, T+1):
    N = float(input())
    res = ''
    cnt = -1

    while N !=0:
        if N>=2**cnt:
            N-=2**cnt
            res += '1'
            cnt -= 1
        else:
            res += '0'
            cnt -= 1
        if len(res) >= 13:
            res = 'overflow'
            break
    print(f'#{tc} {res}')