def cal(v1, v2, i):
    if i == '+':
        return v1 + v2


def step1(mod):
    ST = []
    result = []

    for i in mod:
        if i.isdigit():
            result.append(i)
        else:
            if ST:
                result.append(ST.pop())
                ST.append(i)
            else:
                ST.append(i)
    while ST:
        result.append(ST.pop())
    return result

def step2(lst):
    ST = []
    for i in lst:
        if i.isdigit():
            ST.append(int(i))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1, v2, i))

    return ST[-1]



for tc in range(1, 10+1):
    N = int(input())
    mod = list(input())
    lst = step1(mod)
    print(f'#{tc} {step2(lst)}')