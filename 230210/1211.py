import sys
sys.stdin=open('input.txt','rt')

for _ in range(1, 10 + 1):
    tc = int(input())
    lad = [list(map(int, input().split())) for _ in range(100)]

    x = 0
    min_mov = 10000000

    for j in range(100):
        if lad[0][j] == 1:
            cnt = 0
            col = j

            for row in range(100):
                if col < 99 and lad[row][col + 1] == 1:  # 99의 경우 +1을 할 수가 없음
                    while col < 99 and lad[row][col + 1] == 1:
                        col += 1
                        cnt += 1

                elif col > 0 and lad[row][col - 1] == 1: # 0의 경우 -1을 할 수가 없음
                    while col > 0 and lad[row][col - 1] == 1:
                        col -= 1
                        cnt += 1
            if cnt < min_mov:
                min_mov = cnt
                x = j

    print(f'#{tc} {x}')
