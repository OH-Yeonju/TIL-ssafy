nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10

c = [0, 1]
def partial(k, curS):
    if curS > 10:    # 여기서 백트래킹
        return
    if k == N:    # 여기는 재귀를 빠져나올수있게
        sumV = 0
        if curS == 10:
            for i in range(N):
                if a[i]:
                    print(nums[i], end=' ')
                    sumV += nums[i]
            print('=>', sumV)
        return

    a[k] = 0    # 부분집합에 존재한다 안한다 표시
    partial(k+1, curS)   # N까지 갈 수 있게 계속 반복
    a[k] = 1
    partial(k+1, curS+nums[k])

    # for i in range(2):
    #     a[k] = c[i]
    #     partial(k+1)


a = [-1] * N
partial(0, 0)