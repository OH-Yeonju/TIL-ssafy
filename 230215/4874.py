def cal(v1, v2, i):
    if i == '+':
        return v1 + v2
    if i == '-':
        return v1 - v2
    if i == '*':
        return v1 * v2
    if i == '/':
        return int(v1 / v2)


def forth(lst):
    ST = []
    for i in lst:
        if i.isdigit():
            ST.append(int(i))
        else:
            if len(ST)<2:
                return 'error'
            else:
                v2 = ST.pop()
                v1 = ST.pop()
                ST.append(cal(v1, v2, i))

    if len(ST) > 1:
        return 'error'
    else:
        return ST[-1]



T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())
    if '.' not in lst:
        print(f'#{tc} error')
        break
    lst.pop(-1)
    print(f'#{tc} {forth(lst)}')

