lst = [0]*30
lst[0] = 1
lst[1] = 3
for i in range(30):
    if i > 1:
        lst[i] = lst[i-1] + lst[i-2]*2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {lst[N//10-1]}')

