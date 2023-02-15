# # loop 이용하여 확인하고 부분집합 생성하는 방법
# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[2] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = 1
#                 print(bit)

# 백트래킹으로 순열 구하기
# 순열 생성하기
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k+1):
            print(a[i], end=' ')
            print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1,k):   # 앞에서 사용한 숫자 팡ㄱ
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):  # 남은 숫자를 후보로 추천
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates




NMAX = 11
MAXCANDIDATES = 10
a = [0] * NMAX
backtrack(a, 0, 3)
