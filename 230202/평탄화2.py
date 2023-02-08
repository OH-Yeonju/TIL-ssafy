def max_n(lst):
    maxV = 0
    for i in range(len(lst)):
        if maxV < lst[i]:
            maxV = lst[i]
    return maxV

def min_n(lst):
    minV = 1000
    for i in range(len(lst)):
        if minV > lst[i]:
            minV = lst[i]
    return minV

for i in range(1, 10 + 1):
    dump = int(input())
    nums = list(map(int, input().split()))

    for j in range(dump):
        max_num = max_n(nums)
        min_num = min_n(nums)
        max_idx = nums.index(max_num)
        min_idx = nums.index(min_num)
        nums[max_idx] -= 1
        nums[min_idx] += 1

    a = max_n(nums) - min_n(nums)
    print(f'#{i}', a)