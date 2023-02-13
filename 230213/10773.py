K = int(input())
stack = []
for _ in range(K):
    N = int(input())
    if N != 0:
        stack.append(N)
    else:
        if len(stack) > 0:
            stack.pop(-1)



print(sum(stack))