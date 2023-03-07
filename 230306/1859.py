T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    i = N-1
    j = i-1
    cnt = 0

    while True:
        if j < 0:
            break
        if lst[i] > lst[j]:
            cnt += (lst[i]-lst[j])
            j -= 1
        else:
            i = j
            j -= 1

    print(f'#{tc} {cnt}')


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     answerlst = []
#
#     i = N - 1
#     j = i - 1
#
#     while True:
#         if j < 0:
#             break
#         if numbers[i] > numbers[j]:
#             answerlst.append(numbers[i] - numbers[j])
#             j -= 1
#         else:
#             i = j
#             if i >= 0:
#                 j = i - 1
#     print(f'#{tc} {sum(answerlst)}')