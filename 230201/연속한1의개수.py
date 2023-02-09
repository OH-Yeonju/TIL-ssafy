T = int(input())

for tc in range(1, T + 1):
    le = int(input())
    nums = input()
    cnt = 0
    maxCnt = 0

    for i in range(0, le):
        if nums[i] == '1':
            cnt += 1
            # if maxCnt < cnt:
            #     maxCnt = cnt
        elif nums[i] == '0':
            # if maxCnt < cnt:
            #     maxCnt = cnt
            cnt = 0
        if maxCnt < cnt:
            maxCnt = cnt

    print(f'#{tc} {maxCnt}')