k = 4
N = 8
nums = [0, 4, 1, 3, 1, 2, 4, 1]
res = [-1] * N  # 빈 공간을 준비.. 디버깅 위해 안쓰는 데이터 넣어줌..
  # >i: 0  [1]  2  3  [4]  [5]  6  7 [8]
  # >  [0,  1,  1 ,1 , 2 ,  3 , 4 ,4]

counts = [0] * (k+1) # << 최대값 기준
for num in nums:
    counts[num] += 1
print(counts)

for i in range(k):
    counts[i+1] = counts[i+1] + counts[i]
print(counts)

for i in range(N-1, -1, -1):  # 0을 포함하고 역으로
    num = nums[i]  # i = 7일때 num = 1
    pos = counts[num] # pos = counts[1] = 4
    res[pos-1] = num  # res[4-1] = num = 1
    counts[num] -= 1  # counts[1] = 4 - 1
print(res)