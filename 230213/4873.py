T = int(input())


for tc in range(1, T+1):
    word = list(map(str, input()))
    stack = []

    for i in word:
        if len(stack) > 0:
            if i == stack[-1]:
                stack.pop(-1)
                continue
        stack.append(i)

    print(f'#{tc} {len(stack)}')