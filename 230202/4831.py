T = int(input())

for i in range(1, T +1):
    stop, end, charge = map(int, input().split())
    # stop = 한번에 이동할수있는 end = 종점 charge = 충전기 개수
    chars = list(map(int, input().split()))
    busstop = []
    for i in range(1, 101):
        if stop * i <= end:
            busstop.append(stop*i)
    print(busstop)
    cha_cnt = 0
    for i in range(1, len(busstop)+1):
        for j in chars:
            if j <=  and j < i + stop:
                cha_cnt += 1

    print(cha_cnt)