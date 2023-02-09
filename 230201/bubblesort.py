# 작은 수에서 큰 수로 정렬
nums = [55, 7, 78, 12, 42]
N = 5

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

# 0번째부터 채운다면 작은수에서 큰수로 bubble정렬