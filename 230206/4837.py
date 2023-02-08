T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 12+1))
    cnt = 0
    for i in range(1 << 12):
        lst = []
        lst_sum = 0
        for j in range(12):
            if i & (1<<j):
                lst.append(A[j])
                lst_sum += A[j]
        if len(lst) == N and lst_sum == K:
            cnt += 1
    print(f'#{tc} {cnt}')


# TC = int(input())
# N = 12
#
# for tc in range(1, TC+1):
#     cnt = 0
#     ARR = list(range(1, 12+1))
#     N, K = map(int, input().split())
#     for n in range(1<<N):
#         sumV = 0
#         j_lst = []
#         for j in range(N):
#             r = n & (1<<j)
#             if r != 0:
#                 j_lst.append(ARR[j])
#                 sumV += ARR[j]
#         if len(j_lst) == N and sumV == K:
#             cnt += 1
#     print(f'#{tc} {cnt}')

