import sys
sys.stdin=open('input.txt', 'rt')


def isPelindrome(s):
    lenS = 0
    for _ in s:
        lenS += 1
    for idx in range(lenS // 2):
        if s[idx] != s[lenS-1-idx]:
            return 0
    return 1

def check(N, M):
    maxle = 0
    sle = 0
    for row in range(N):
        for st in range(N-M+1):
            temp = ''
            for col in range(M):
                temp += arr[row][st+col]
            if isPelindrome(temp):
                sle = M
            if maxle < sle:
                maxle = sle

    for col in range(N):
        for st in range(N-M+1):
            temp = ''
            for row in range(M):
                temp += arr[st+row][col]
            if isPelindrome(temp):
                sle = M
            if maxle < sle:
                maxle = sle
    return maxle


for _ in range(1, 10+1):
    num = int(input())
    arr = [list(input()) for _ in range(100)]
    cnt = 0

    for i in range(1, 100+1):
        M = i
        c = check(100, M)
        if c > cnt:
            cnt = c


    print(f'#{_} {cnt}')