def isPelindrome(s):
    # s = s.rstrip()
    lenS = 0
    for _ in s:
        lenS += 1
    for idx in range(lenS // 2):
        if s[idx] != s[lenS - 1 - idx]:
            return 0
    return 1


def check(N, M):
    for row in range(N):
        for st1 in range(N - M + 1):
            temp = ''
            for col in range(M):
                temp += arr[row][st1 + col]
            if isPelindrome(temp):
                # res = temp
                return temp

    for col in range(N):
        for st2 in range(N - M + 1):
            temp = ''
            for row in range(M):
                temp += arr[st2 + row][col]
            if isPelindrome(temp):
                # res = temp
                return temp


TC = int(input())
for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    arr = []
    for i in range(N):
        arr.append(list(input()))
    print(f'#{tc} {check(N, M)}')