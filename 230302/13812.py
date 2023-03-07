T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst = sorted(lst)
    per = 0
    for i in range(N):
        per += 1
        b = lst[i]//M * K
        if b-per < 0:
            print(f'#{tc} Impossible')
            break
        if i == N-1 and b-per>=0:
            print(f'#{tc} Possible')