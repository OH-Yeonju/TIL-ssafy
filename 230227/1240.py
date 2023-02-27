T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mapping = {'0':'0001101', '1':'0011001', '2':'0010011', '3':'0111101',
               '4':'0100011', '5':'0110001', '6':'0101111', '7':'0111011',
               '8':'0110111', '9':'0001011'}
    lst = [input() for _ in range(N)]

    num = ''
    for i in lst:
        if '1' in i:
            num = i

    idx = 0
    for i in range(M-1, -1, -1):
        if num[i] == '1':
            idx = i
            break

    num = num[idx-56+1:idx+1]

    sec = ''
    for i in range(8):
        a = num[7*i:7*(i+1)]
        for key, value in mapping.items():
            if mapping[key] == a:
                sec += key


    sumV = 0
    sumV2 = 0
    for i in range(4):
        n1 = sec[2*i]
        n2 = sec[2*i+1]
        sumV += int(n1)
        sumV2 += int(n2)

    if (sumV*3 + sumV2) % 10 == 0:
        r = 0
        for i in sec:
            r += int(i)
        print(f'#{tc} {r}')
    else:
        print(f'#{tc} 0')