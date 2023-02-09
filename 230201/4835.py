# import sys
# sys.stdin = open("파일명.txt", "r")

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    s_lst = []
    for j in range(len(nums)-M+1): # 주어진 숫자들
        n_lst = nums[j:j+M]
        a = 0
        for k in n_lst:
            a += k
        s_lst.append(a)
    print(s_lst)
    maxNum = 0
    minNum = 1000000000
    for num in s_lst:
        if maxNum < num:
            maxNum = num
        if minNum > num:
            minNum = num
    print(f'#{i} {maxNum-minNum}')

