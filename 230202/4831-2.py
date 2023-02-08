TC = int(input())
for t in range(1, TC + 1):
    K, N, M = map(int, input().split())
    CHS = list(map(int, input().split()))

    curV = 0
    cnt = 0
    while curV < N:
        nextV = curV + K
        if nextV >= N:
            break

        if nextV in CHS:
            curV = nextV
            cnt += 1
        else:
            while nextV not in CHS and curV < nextV:
                nextV -= 1
                if curV == nextV:
                    cnt = 0
                    break
                else:
                    curV = nextV
                    cnt += 1
    print(f'#{t} {cnt}')