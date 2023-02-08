def lstsum(lst):
    a = 0
    for i in lst:
        a += i
    return a

def lstmax(lst):
    m = 0
    for i in lst:
        if m < i:
            m = i
    return m

def lstidx(lst):
    idx = 0
    for i in range(len(lst)):
        if lstmax(lst) == lst[i]:
            idx = i
    return idx

T = int(input())

for tc in range(1, T+1):
    days = int(input())
    price_lst = list(map(int, input().split()))
    maxV = 0

    while True:
        idx = lstidx(price_lst)
        maxV += price_lst[idx]*idx - lstsum(price_lst[:idx])
        price_lst = price_lst[idx+1:]
        if price_lst == []:
            break

    print(f'#{tc} {maxV}')
