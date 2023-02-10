T = int(input())

for tc in range(1, 10+1):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    maxS = 0
    if N < M:
        for j in range(M-N+1):
            score = 0
            for k in range(N):
                score += lst1[k]*lst2[j+k]
            if score > maxS:
                maxS = score

    if N > M:
        for j in range(N-M+1):
            score = 0
            for k in range(M):
                score += lst2[k]*lst1[j+k]
            if score > maxS:
                maxS = score

    print(f'#{tc} {maxS}')