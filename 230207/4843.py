T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N-1):
        minIdx = i
        for j in range(i + 1, N):
            if nums[minIdx] > nums[j]:
                minIdx = j
        nums[i], nums[minIdx] = nums[minIdx], nums[i]

    l_lst = []
    for i in range(N//2):
        l_lst.append(nums[-1-i])
        l_lst.append(nums[0+i])

    print(f'#{tc}', *l_lst[:10])