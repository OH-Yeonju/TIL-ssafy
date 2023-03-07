T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    minV = 1000
    size = [0] * 31  # 당근의 크기 1~30
    for c in arr:
        size[c] += 1

    for i in range(29):         # i 1~28 소박스에 들어갈 마지막 크기 i
        for j in range(30):     # i+1~29 중박스에 들어갈 마지막 크기 j
            A = sum(size[1:i+1])
            B = sum(size[i+1:j+1])
            C = sum(size[j+1:31])

            if A*B*C != 0 and A<=N//2 and B<=N//2 and C<=N//2:
                diff = max(A, B, C) - min(A, B, C)
                if diff < minV:
                    minV = diff
    if minV == 1000:
        minV = -1
    print(f'#{tc} {minV}')




    # # 오름차순정렬
    # arr.sort()
    #
    # minV = 1000
    # for i in range(0, N-2):
    #     for j in range(i+1, N-1):
    #         if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
    #             A = i+1
    #             B = j-i
    #             C = N-1-j
    #             if A*B*C!=0 and A<=N//2 and B<=N//2 and C<=N//2:  # 빈 박스 없고 절반 초과하는 박스도 없으면
    #                 if minV > max(A, B, C) - min(A, B, C):
    #                     minV = max(A, B, C) - min(A, B, C)
    #
    # if minV == 1000:
    #     minV = -1
    # print(f'#{tc} {minV}')