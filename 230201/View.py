import sys
sys.stdin = open("input.view.txt", "r")


for tc in range(1, 10+1):
    num = int(input())
    building = list(map(int, input().split()))
    view_lst = []
    for i in range(2, num-2):
        if building[i] > building[i-1] and building[i] > building[i-2] and building[i] > building[i+1] and building[i] > building[i+2]:
            view_lst.append(building[i-2:i+3])

    nums_lst = []
    num_sum = 0
    for num_lst in view_lst:
        for i in range(4, 0, -1):
            for j in range(0, i):
                if num_lst[j] > num_lst[j+1]:
                    num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]
        num_sum += (num_lst[4]-num_lst[3])

    # num_sum = 0
    # for i in nums_lst:
    #     num_sum += i
    print(f'#{tc} {num_sum}')