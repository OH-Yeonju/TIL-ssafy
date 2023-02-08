def my_abs(value):
    if value<0:
        return value*(-1)
    return value

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int,input().split())) for _ in range(N)]

    # 위, 아래, 왼, 오른
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    sumV = 0
    for row in range(N):
        for col in range(N):
            for d in range(4):
                newR = row + dr[d]
                newC = col + dc[d]
                # if 정상범위가 아니라면:
                # continue
                if 0<=newR<N and 0<=newC<N: # 정상범위라면
                    newV = ARR[newR][newC]
                # sumV += abs(ARR[row][col] - ARR[newR][newC])
                    sumV += my_abs(ARR[row][col] - ARR[newR][newC])

    print(tc, sumV)