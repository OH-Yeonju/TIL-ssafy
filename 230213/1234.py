for tc in range(1, 10+1):
    N, word = map(str, input().split())
    stack = []
    for i in range(int(N)):
        if len(stack) > 0:
            if word[i] == stack[-1]:
                stack.pop(-1)
                continue
        stack.append(word[i])

    print(f'#{tc}', ''.join(stack))