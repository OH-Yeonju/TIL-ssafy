import sys
sys.stdin=open('input.txt', 'rt')

# 회문 구하는 함수
def isPelindrome(s):
    s = s.rstrip()
    lenS = 0
    for _ in s:
        lenS +=1

    idx = 0
    while idx<lenS//2 and s[idx] == s[lenS-1-idx]:
        idx += 1

    if idx == lenS//2:
        return 1
    return 0


def check(N):
    for row in range(N):
        for st in range(99, -1, -1):
            temp = ''
            for col in range(N):
                temp += arr[row][st + col]
            if isPelindrome(temp):
                # res = temp
                return temp

    for col in range(N):
        for st in range(99, -1, -1):
            temp = ''
            for row in range(N):
                temp += arr[st + row][col]
            if isPelindrome(temp):
                # res = temp
                return temp


for _ in range(10):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(100)]

    print(check(100))






