T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    for _ in range(M):
        v = lst.pop(0)
        lst.append(v)
    print(f'#{tc} {lst[0]}')