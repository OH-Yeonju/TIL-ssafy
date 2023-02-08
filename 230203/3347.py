T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    price_lst = list(map(int, input().split()))
    com = list(map(int, input().split()))
    vote = [0] * len(price_lst)
    for i in com:
        for j in range(len(price_lst)):
            if price_lst[j] <= i:
                vote[j] += 1
                break
    print(vote)
    maxV = 0
    cnt = 0
    for i in range(len(vote)):
        if maxV < vote[i]:
            maxV = vote[i]
            cnt = i

    print(f'#{tc} {cnt+1}')

