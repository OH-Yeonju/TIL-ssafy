def inpair(word):
    stack = []
    for i in word:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)

        elif i == ')':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '(':
                return 0

        elif i == ']':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '[':
                return 0

        elif i == '}':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '{':
                return 0

        elif i == '>':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '<':
                return 0

    if len(stack) > 0:
        return 0
    return 1


for tc in range(1, 10+1):
    N = int(input())
    word = list(map(str, input()))
    print(f'#{tc} {inpair(word)}')