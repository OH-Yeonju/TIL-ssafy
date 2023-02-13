def inPair(word):
    stack = []
    for c in word:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '(':
                return 0

        if c == '{':
            stack.append(c)
        elif c == '}':
            if len(stack) == 0:
                return 0
            t = stack.pop(-1)
            if t != '{':
                return 0

    if len(stack) > 0:
        return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    word = list(map(str, input()))

    print(f'#{tc} {inPair(word)}')
