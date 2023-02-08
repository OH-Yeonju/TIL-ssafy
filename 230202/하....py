TC = int(input())
for tc in range(1, TC + 1):
    K, N, M = map(int, input().split())
    CHS = list(map(int, input().split()))

    cnt = 0
    curV = 0

    while curV < N:
        nextV = curV + K
        # 끝까지 가서 끝나는 경우
        if nextV >= N:
            break
        # 충전소가 없지만 다음 멈추는 구간보다는 적은 경우
        while nextV not in CHS and nextV > curV:
            nextV -= 1

        # 충전소가 아예 없는 경우
        if nextV == curV:
            cnt = 0
            break

        # 있는 경우
        curV = nextV
        cnt += 1

    print(f'#{tc} {cnt}')
