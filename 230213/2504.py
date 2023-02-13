def isPair(per):
    stack = []
    cir = 0
    squ = 0
    cis = 0
    cic = 0
    sic = 0
    sis = 0
    for i in range(len(per)):
        if per[i] == '(' or '[':
            stack.append(per[i])
        elif per[i] == ')':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '(':
                return 0
            if per[i-1] == '(' and per[i+1] == ']' and per[i-2] == '[':
                cis += 1
            if per[i-1] == '(' and per[i+1] == ')' and per[i-2] == '(':
                cic += 1
            else:
                cir += 1
        elif i == ']':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '[':
                return 0
            if per[i-1] == '[' and per[i+1] == ')' and per[i-2] == '(':
                sic += 1
            if per[i-1] == '[' and per[i+1] == ']' and per[i-2] == '[':
                sis += 1
            else:
                squ += 1
    if len(stack) > 0:
        return 0
    return squ*3 + cir*2 + (cis+sic)*6 + cic*4 + sis*9




per = list(map(str, input()))
print(isPair(per))