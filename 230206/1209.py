import sys
sys.stdin = open("input.txt", "r")

for t in range(10):
    M = 100
    N = 100
    tc = int(input())
    l = [list(map(int, input().split())) for _ in range(M)]
    maxV = 0
    for row in range(0, M):
        sumV = 0
        sumC = 0
        sumX = 0
        sumY = 0
        for col in range(0, N):
            sumV += l[row][col]
            sumC += l[col][row]
            sumX += l[col][col]
            sumY += l[col][99-col]
            if maxV < sumV:
                maxV = sumV
            if maxV < sumC:
                maxV = sumC
            if maxV < sumX:
                maxV = sumX
            if maxV < sumY:
                maxV = sumY

    print(f'#{tc} {maxV}')


