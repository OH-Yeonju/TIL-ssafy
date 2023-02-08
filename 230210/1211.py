import sys
sys.stdin=open('input.txt','rt')

for _ in range(1, 10+1):
    tc = int(input())
    lad = [list(map(int, input().split())) for _ in range(100)]

    cl = 0
    cnt = 0
    x = 0
    min_mov = 10001

    for j in range(100):
        if lad[0][j] == 1:
            col = j
            cl = j

            for row in range(0, 100):
                if col+1<100 and lad[row][col+1] == 1:
                    while col+1<100 and lad[row][col+1] == 1:
                        col += 1
                        cnt += 1

                if col-1>=0 and lad[row][col-1] == 1:
                    while col-1>=0 and lad[row][col-1] == 1:
                        col -= 1
                        cnt += 1

            print(j, cnt)


            if cnt < min_mov:
                min_mov = cnt
                x = cl
            cnt = 0




    print(f'#{tc} {x}')
