TC = int(input())
for t in range(1, TC + 1):
    K, N, M = map(int, input().split())
    CHS = list(map(int, input().split()))

    curV = 0
    cnt = 0
    # 1. 다음 충전 위치 찾기
    while curV < N:
        nextV = curV + K
        # 목표에 도달한 경우
        if nextV >= N:
            break

        # if nextV not in CHS
        while curV < nextV and nextV not in CHS:
            nextV -= 1

        # 2. 충전기가 없는 경우 : curV와 curV + K 사이에 충전기가 없음
        if curV == nextV:
            cnt = 0
            break

        # 3. 찾은 경우 충전
        curV = nextV
        cnt += 1

    print(f'#{t} {cnt}')