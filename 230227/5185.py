def hextobin(s):
    # 16진수를 10진수로
    if s.isdigit():
        decV = int(s)

    else:
        decV = ord(s) - ord('A') + 10

    # 10진수를 2진수로
    res = ''
    for j in range(3, -1, -1):
        res += '1' if decV & (1 << j) else '0'

    return res



T = int(input())

for tc in range(1, T+1):
    N, N2 = input().split()
    res = ''
    for i in N2:
        res +=hextobin(i)

    print(f'#{tc} {res}')