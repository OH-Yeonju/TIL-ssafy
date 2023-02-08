T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    counts = [0] * 10
    for num in nums:
        counts[num] += 1

    maxV = 0
    for i in range(10):
        if maxV <= counts[i]:
            maxV = counts[i]
            maxI = i

    print(f'#{tc} {maxI} {maxV}')