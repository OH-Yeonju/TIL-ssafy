import sys
sys.stdin = open('input.txt', 'rt')

def pd(s):
    lenS = 0
    for _ in s:
        lenS += 1
    for idx in range(lenS // 2):
        if s[idx] != s[lenS-1-idx]:
            return 0
    return 1


def check(N, M):
    cnt = 0
    for row in range(N):
        for st1 in range(N-M+1):
            temp = ''
            for col in range(M):
                temp += word[row][st1+col]
            if pd(temp):
                cnt += 1

    for col in range(N):
        for st2 in range(N - M + 1):
            temp = ''
            for row in range(M):
                temp += word[st2 + row][col]
            if pd(temp):
                # res = temp
                cnt += 1

    return cnt



for tc in range(1, 10+1):
    num = int(input())
    word = [list(input()) for _ in range(8)]
    c = check(8, num)
    print(f'#{tc} {c}')
