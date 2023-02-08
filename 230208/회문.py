def ispenlindrome(s):
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

T = int(input())

for tc in range(1, T + 1):
    N = input()
    print(f'#{tc} {ispenlindrome(N)}')


# T = int(input())
#
# for tc in range(1, T + 1):
#     N = input()