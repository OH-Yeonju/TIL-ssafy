T = int(input())

for tc in range(1, T+1):
    le = input()

    f_cnt = 0
    cnt = 0
    for i in range(len(le)):
        if le[i] == '(':
            cnt += 1
        else:
            if le[i-1] == '(':
                cnt -= 1
                f_cnt += cnt
            else:
                cnt -= 1
                f_cnt += 1
    print(f'#{tc} {f_cnt}')