T = int(input())

for tc in range(1, T+1):
    nums = list(map(str, input()))
    reset = ['0']*len(nums)
    cnt = 0
    for i in range(len(nums)):
        if nums[i] != reset[i]:
            reset = reset[:i] + ([nums[i]]*(len(nums)-i))
            cnt += 1
        if nums == reset:
            break
    print(f'#{tc} {cnt}')