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
    print(nums)
    counts = [0] * (100+1)  # << 최대값 기준
    for num in nums:
        counts[num] += 1
    print(counts)

    for i in range(100):
        counts[i + 1] = counts[i + 1] + counts[i]
    print(counts)

    res = [-1]*100
    for i in range(99, -1, -1):
        num = nums[i]
        pos = counts[num]
        res[pos - 1] = num
        counts[num] -= 1
    print(res)  # 순서대로...

    for i in range(dump):
        max_box = max_n(res)
        min_box = min_n(res)
        max_idx = res.index(max_box)
        min_idx = res.index(min_box)
        res[max_idx] -= 1
        res[min_idx] += 1
    print(res)







    # for i in range(dump):
    #     max_n = res[-1]
    #     min_n = res[0]
    #     for n in res:
    #         if max_n < n:
    #             max_n = n
    #         break
    #     for n in res:
    #         if min_n > n:
    #             min_n = n
    #         break
    #
    #     for j in range(len(res)):
    #         if res[j] == max_n:
    #             res[j] -=1
    #         break
    #     for j in range(len(res)):
    #         if res[j] == min_n:
    #             res[j] += 1
    #         break
    #     print(res)