nums = [64, 25, 10, 22, 11]
N = 5

# minV = nums[0]
# for i in range(N):
#     if minV > nums[i]:
#         minV = nums[i]
#         minIdx = i
#
# minIdx = 0
# for i in range(N):
#     if nums[minIdx] > nums[i]:
#         minIdx = i
#

for i in range(N-1):
    minIdx = i
    for j in range(i, N):
        if nums[minIdx] > nums[j]:
            minIdx = j

    nums[minIdx], nums[i] = nums[i], nums[minIdx]

print(nums)
