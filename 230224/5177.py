def enq(item):
    global last
    last += 1
    TREE[last] = item
    c = last
    p = last // 2
    while p>=1 and TREE[p] > TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = c//2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    TREE = [0] * (N+1)
    last = 0
    lst = list(map(int, input().split()))
    for i in lst:
        enq(i)
    print(TREE)

    sumV = lst[1]
    num = N
    while num > 1:
        sumV += lst[num//2]
        num = num//2
    print(sumV)