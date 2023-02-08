# s = input()
# cnt = [0] * 10
# for c in s:
#     cnt[int(c)] += 1
#
# print(cnt)

# m = []
# m.append(input())
# m.append(input())
# print(m)

# 1차원
# "1232" > [1, 2, 3, 2]
# l = list(map(int, input()))

# 2차원
# s = [input() for _ in range(5)]

# 1, 4X3 이차원 배열을 입력
'''
12 34 32
34 45 32
12 34 32
34 45 32
'''
M = 4
N = 3
l = [list(map(int, input().split())) for _ in range(M)]
# print(l)
# 행우선출력
for i in range(0, M):
    for col in range(0, N):
        print(l[i][col])

# 열우선출력
for i in range(0, N):
    for row in range(0, M):
        print(l[row][i])
        
# i번째 low의 합 구하기
sumV = 0
for col in range(0, N):
    sumV += l[i][col]

# low 합 구하기
maxV = 0
for row in range(0, M):
    sumV = 0
    for col in range(0, N):
        sumV += l[row][col]
    # 전체 합 출력하기
    print(sumV)
    # 합 중 최대값 구하기
    if maxV < sumV:
        maxV = sumV
print(maxV)


for i in range(N):
    sumV = 0
    for row in range(M):
        sumV += l[row][i]

#N과 M이 같다면
for i in range(N):
    sumR = 0
    sumC = 0
    for j in range(N):
        sumR += l[i][j]
        sumC += l[j][i]


