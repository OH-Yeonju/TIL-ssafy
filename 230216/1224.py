def step1(mat):
    ST = []
    result = []
    isp = {'+':1, '*':2, '(':3}  # 밖에서넣을때
    icp = {'+':1, '*':2, '(':0}  # 안에있을때

    for i in mat:
        if i.isdigit():
            result.append(i)
        elif i == ')':
            while ST and ST[-1] != '(':
                result.append(ST.pop())
            ST.pop()
        else:
            if ST and icp[ST[-1]] >= isp[i]:
                while ST and icp[ST[-1]] >= isp[i]:
                    result.append(ST.pop())
                ST.append(i)
            else:
                ST.append(i)
    while ST:
        result.append(ST.pop())
    return result

def step2(mat):
    ST = []

    for i in mat:
        if i.isdigit():
            ST.append(int(i))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1, v2, i))
    return ST[-1]

def cal(v1, v2, i):
    if i == '+':
        return v1 + v2
    if i == '*':
        return v1 * v2


for tc in range(1, 10+1):
    N = int(input())
    mat = input()
    res = step2(step1(mat))

    print(f'#{tc} {res}')
