nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10

c = [0, 1]
def partial(k, curS):   # k까지 왔을 때 합을 표시
    if curS > 10:
        return
    if k==N:    # 재귀 끝낼 조건
        print(a, '=>', end=' ')
        print(curS)
        if curS == 10:
            for i in range(N):
                if a[i] == 1:
                    print(nums[i], end=' ')
            print()
            # print(a)
        # sumV = 0
        # for i in range(N):
        #     print(nums[i], end=' ')
        #     if a[i]:
        #         sumV += nums[i]
        # print(sumV)
        return

    a[k] = 0
    partial(k+1, curS)
    a[k] = 1
    partial(k+1, curS + nums[k])

    # for i in range(2):
    #     a[k] = c[i]
    #     if c[i] == 1:   # 부분집합 안에 숫자가 존재시./.
    #         partial(k+1, curS+nums[k])
    #     else:
    #         partial(k+1, curS)


a = [-1] * N   #goal[i] 정답의 i번쨰 데이터
partial(0, 0)