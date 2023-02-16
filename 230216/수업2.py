nums = [20, 30, 40]

def per(k):
    if k==N:
        print(a)
        for i in range(N):
            idx = a[i]
            print(nums[idx], end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            a[k] = i
            per(k+1)
            visited[i] = False    # 원상복구

    # a[k] = 1
    # per(k+1)
    # a[k] = 0
    # per(k+1)

N = 3
a = [-1] * N
visited = [False] * N

print(per(0))