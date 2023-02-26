def enq(item):
    global last
    last += 1
    TREE[last] = item
    c = last
    p = c//2
    while p>=1 and TREE[c] < TREE[p]:
        TREE[c], TREE[p] = TREE[p], TREE[c]
        c = p
        p = c//2



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    TREE = [0] * 1000001
    last = 0

    for item in lst:
        enq(item)

    sumV = 0
    c = N
    p = N // 2
    while p >= 1:
        sumV += TREE[p]
        c = p
        p = c//2

    print(f'#{tc} {sumV}')