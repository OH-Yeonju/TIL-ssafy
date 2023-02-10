T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 정렬부터
    for i in range(N-1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    n_nums = []
    for i in range(N//2):
        n_nums.append(nums[N-1-i])
        n_nums.append(nums[i])

    print(f'#{tc}', *n_nums[:10])