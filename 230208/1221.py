import sys
sys.stdin=open('input.txt', 'rt')

T = int(input())
num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T + 1):
    N, M = map(str, input().split())
    N = int(N.lstrip('#'))
    M = int(M)
    nums = list(map(str, input().split()))
    n_nums = []
    for i in nums:
        for key, value in num.items():
            if i == key:
                n_nums.append(value)

    res = [-1]*M
    counts = [0]*10
    for n in n_nums:
        counts[n] += 1

    for i in range(9):
        counts[i+1] = counts[i+1] + counts[i]

    for i in range(M-1, -1, -1):
        n = n_nums[i]
        pos = counts[n]
        res[pos-1] = n
        counts[n] -= 1

    f_num = []
    for i in res:
        for key, value in num.items():
            if i == num[key]:
                f_num.append(key)

    print(f'#{N}')
    print(*f_num)