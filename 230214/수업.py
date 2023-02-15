# n! = n * (n-1)!
# n**m = n * n**m-1

def mul(n, m):
    if m == 1:
        return n
    return n*mul(n, m-1)

print(mul(5, 3))


def factorial(n):
    if n == 1:
        return 1
    t = n * factorial(n-1)
    return t

print(factorial(5))


#피보나치 : 0 1 1 2 3 5 8 ...
# 일반적 재귀
# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     t1 = fibo(n-1)
#     t2 = fibo(n-2)
#     return t1 + t2

# memoization
# fi = [0]*100
# fi[0] = 0
# fi[1] = 1
#
# def fibo(n):
#     if n >= 2 and fi[n]==0 : # 이미 계산이 되어있지 않다면
#         t1 = fibo(n-1)
#         t2 = fibo(n-2)
#         fi[n] = t1 + t2
#
#     return fi[n]
#
# print(fibo(6))

# DP
def fibo(n):
    fi = [0] * 100
    fi[0] = 0
    fi[1] = 1
    for i in range(2, n+1):
        fi[i] = fi[i-1] + fi[i-2]
    return fi[n]

print(fibo(6))