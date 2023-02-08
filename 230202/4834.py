T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    counts = [0] * 10
    for num in nums:
        counts[num] += 1

    maxV = 0
    for n in counts:
        if maxV < n:
            maxV = n # 가장 많은 카드의 장수

    for i in range(9):
        counts[i + 1] = counts[i + 1] + counts[i]
    res = [-1] * N
    for i in range(N - 1, -1, -1):
        num = nums[i]
        pos = counts[num]
        res[pos - 1] = num
        counts[num] -= 1

    card_dict = {}
    for i in res:
        if i in card_dict:
            card_dict[i] += 1
        else:
            card_dict[i] = 1

    maxIdx = 0
    for key, value in card_dict.items():
        if card_dict[key] == maxV:
            maxIdx = key

    print(f'#{tc} {maxIdx} {maxV}')

