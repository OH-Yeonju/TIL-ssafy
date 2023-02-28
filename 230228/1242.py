import sys
sys.stdin=open('input.txt', 'rt')

def hextobin(s):
    if s.isdigit():
        decV = int(s)
    else:
        decV = ord(s) - ord('A') + 10
    res = ''
    for j in range(3, -1, -1):
        res += '1' if decV & (1<<j) else '0'
    return res

mapping = {'0':'0001101', '1':'0011001', '2':'0010011', '3':'0111101',
           '4':'0100011', '5':'0110001', '6':'0101111', '7':'0111011',
           '8':'0110111', '9':'0001011'}
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    sec = []

    for i in lst:
        # word = ''
        # for j in i:
        #     if j !='0':
        #         word += j
        #     else:
        #         if len(word) == 0:
        #             pass
        #         else:
        #             if word not in sec:
        #                 sec.append(word)
        #             word = ''
        if i not in sec:
            sec.append(i)

    htob = []
    for i in sec:
        num = '0000'
        for j in i:
            num += str(hextobin(j))
        htob.append(num)



    ans = ''
    for snum in htob:
        idx = 0
        for i in range(len(snum)-1, -1, -1):
            if snum[i] == '1':
                idx = i
                break
        secnum = snum[idx-55:idx+1]



        tmp = ''
        for i in range(8):
            a = secnum[7*i:7*(i+1)]
            for key, value in mapping.items():
                if mapping[key] == a:
                    tmp += key

        sumV = 0
        sumV2 = 0
        for i in range(7):
            if i%2 == 0:
                sumV += int(tmp[i])
            else:
                sumV2 += int(tmp[i])

        if ((sumV*3) + sumV2 + int(tmp[7])) % 10 == 0:
            ans = tmp

    resV = 0
    for i in ans:
        resV += int(i)

    print(f'#{tc} {resV}')





