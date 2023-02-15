# 재귀 기본 구조
def f(i, k):      # 현재 상태, k = 목표
    if i == k:    # 목표도달하면
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)


A = [10, 20, 30]
B = [0] * 3
f(0, 3)

# A = [i for i in range(1000)]
# B = [0] * 1000
# f(0, 1000)  > 재귀호출 한계에 부딪힘