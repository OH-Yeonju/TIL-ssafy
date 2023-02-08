import sys
sys.stdin=open('input.txt', 'rt')

for _ in range(1, 10+1):
    tc = int(input())
    ARR = [list(map(int, input().split())) for _ in range(100)]
    f_row = 99
    col = 0
    for i in range(100):
        if ARR[99][i] == 2:
            col = i

    for row in range(98, 0, -1):
        if col-1>=0 and ARR[row][col-1] == 1:
            while ARR[row][col-1] == 1:
                col -= 1
        elif col+1<100 and ARR[row][col+1] == 1:
            while col+1<100 and ARR[row][col+1] == 1:
                col += 1


    print(f'#{tc} {col}')