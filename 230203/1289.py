T = int(input())


rest_lst = [0]*8
for i in range(1, T+1):
    money = int(input())
    money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for j in range(len(money_lst)):
        rest_lst[j] = money//money_lst[j]
        money = money - money_lst[j]*rest_lst[j]
        if money == 0:
            break

    print(f'#{i}')
    print(*rest_lst)

