def step1(mat):
    ST = []
    result = []
    isp = {'+':1, '-':1, '*':2, '/':2, '(':3}
    icp = {'+':1, '-':1, '*':2, '/':2, '(':0}

    for i in mat:
        if i.isalpha():
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


word = input()
print(''.join(step1(word)))
