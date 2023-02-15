# exp = '2+3*4/5'
# goal = '234*5/+'
# exp = '(6+5*(2-8)/2)'
# goal = '6528-2/*+'
def step1(exp):
    isp = {'+':1, '-':1, '*':2, '/':2, '(':0}  # 스택 안에 있을 때
    icp = {'+':1, '-':1, '*':2, '/':2, '(':3}  # 스택에 넣을 때


    ST = []
    result = []
    for c in exp:
        if c.isdigit():
            # print(c)
            result.append(c)
        elif c == ')':
            while ST and ST[-1] != '(':
                result.append(ST.pop())
                # print(ST.pop())
            ST.pop()
        else:
            if ST and isp[ST[-1]] >= icp[c]:    # 우선순위 비교, if ST = len(ST)>0
                result.append(ST.pop())
                # print(ST.pop())
                ST.append(c)
            else:
                ST.append(c)

    while ST:
        result.append(ST.pop())
        # print(ST.pop())
    return result

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v1 - v2
    if op == '*':
        return v1 * v2
    if op == '/':
        return v1 / v2

def step2(exp):
    ST = []
    for c in exp:
        if c.isdigit():
            ST.append(int(c))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1, v2, c))

    return ST[-1]


exp = '(6+5*(2-8)/2)'
post = step1(exp)
# print(post)
print(step2(post)) # 최종연산결과