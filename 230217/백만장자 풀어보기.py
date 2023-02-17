T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    i = 0
    sumV = 0

    while i < N:
        maxi = i
        for j in range(i+1, N):  # 중간최대값 구하기.....
            if lst[j] > lst[maxi]:
                maxi = j


        for k in range(i, maxi):
            sumV += lst[maxi] - lst[k]
        i = maxi + 1    # 이 이후부터 시작
    print(f'#{tc} {sumV}')