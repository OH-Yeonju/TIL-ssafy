def cal(lwinner, rwinner):
    l = lwinner[1]
    r = rwinner[1]
    if l * r == 2:
        if l == 2:
            return lwinner
        return rwinner
    if l * r == 3:
        if l == 1:
            return lwinner
        return rwinner
    if l * r == 6:
        if l == 3:
            return lwinner
        return rwinner
    if l == r:
        return lwinner

def game(group):
    if len(group) == 1:
        return group[0]
    else:
        j = len(group) +1
        lgroup = group[:j//2]
        rgroup = group[j//2:]
        lwinner = game(lgroup)
        rwinner = game(rgroup)
        return cal(lwinner, rwinner)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(1, N+1):
        lst[i-1] = (i, lst[i-1])

    print(f'#{tc} {game(lst)[0]}')