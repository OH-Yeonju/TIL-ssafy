T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    minNum = 1000001
    maxNum = 0
    for i in nums:
        if maxNum < i:
            maxNum = i
        if minNum > i:
            minNum = i
    print(f'#{tc} {maxNum-minNum}')