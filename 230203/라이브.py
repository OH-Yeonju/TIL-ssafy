# 버스노선
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     cnts = [0]*5000
#     for _ in range(n):
#         S, E = map(int, input().split())
#         for i in range(s, E+1):
#             cnts[i] += 1
#
#     p = int(input())
#     alst = []
#     for _ in range(P):
#         p = int(input())
#         alst.append(cnts[p])
#
#     print(f'#{test_case}', *alst)



# 소인수분해
# divs = [2, 3, 5, 7, 11]
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     cnts = [0] * len(divs)
#
#     for i in range(len(divs)):
#         while N % divs[i] == 0:
#             cnts[i] += 1
#             N = N // divs[i]
#
#     print(f'#{test_case}', *cnts)