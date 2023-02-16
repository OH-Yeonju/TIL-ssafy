def cal(v1, v2, i):
    if i == '+':
        return v1 + v2
    elif i == '*':
        return v1 * v2

def step1(exp):
    isp = {'+':1, '*':2}

    ST = []
    result = []

    for i in mat:
        if i.isdigit():
            result.append(i)
        else:
            if ST and isp[ST[-1]] >= isp[i]:
                while ST and isp[ST[-1]] >= isp[i]:
                    result.append(ST.pop())
                ST.append(i)
            else:
                ST.append(i)
    while ST:
        result.append(ST.pop())
    return result

def step2(exp):
    ST = []

    for i in exp:
        if i.isdigit():
            ST.append(int(i))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1, v2, i))

    return ST[-1]




for tc in range(1, 10+1):
    N = int(input())
    mat = input()
    res = step2(step1(mat))
    print(f'{tc} {res}')

