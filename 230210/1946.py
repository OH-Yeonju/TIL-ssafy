T = int(input())

for _ in range(1, T+1):
    N = int(input())
    temp = ''
    for i in range(N):
        A, B = map(str, input().split())
        temp += A*int(B)

    le = len(temp) // 10
    print(f'#{_}')
    for i in range(0, le):
        print(temp[10*i:10*(i+1)])
    print(temp[10*le:])