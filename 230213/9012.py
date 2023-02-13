def inpair(par):
    stack = []
    for i in par:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return 'NO'

            t = stack.pop(-1)
            if t != '(':
                return 'NO'
    if len(stack) > 0:
        return 'NO'
    return 'YES'


N = int(input())

for _ in range(N):
    par = list(map(str, input()))
    print(inpair(par))

