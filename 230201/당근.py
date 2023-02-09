T = int(input())

for tc in range(1, T+1):
    le = int(input())
    nums = list(map(int, input().split()))
    cnt = 1
    maxCnt = 1
    for i in range(1, le):
        if nums[i-1] < nums[i]:
            cnt += 1
            if maxCnt < cnt:
                maxCnt = cnt
        elif nums[i-1] > nums[i]:
            cnt = 1
    print(f'#{tc} {maxCnt}')