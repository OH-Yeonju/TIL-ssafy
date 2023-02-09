# 리스트 길이 구하기
def my_len(lst):
    cnt = 0
    for i in lst:
        cnt += 1
    return cnt

blocks = [7, 4, 2, 0, 0, 6, 0, 7, 0]

N = len(blocks)

res = [0] * N
curMaxV = 0
# 요소 하나와 다른 요소들 비교
for i in range(0, N):
    cnt = 0
    # i와 그 다음부터 비교해야함
    for j in range(i+1, N):
        # 작은 수의 갯수를 세야..(낙차구하기)
        if blocks[i] > blocks[j]:
            cnt += 1
    # 낙차와 최대값 비교
    if curMaxV < cnt:
        curMaxV = cnt
print(curMaxV)


#     res[i] = cnt
# print(res)

# 저장된 낙차 중 제일 큰 값을 구한다
# maxV = res[0]
# for i in res:
#     if maxV < i:
#         maxV = i
# print(maxV)



# for i in range(0, N):
#     cnt = 0
#     for j in range(i+1, N):
#         if blocks[i] > blocks[j]:
#             cnt += 1