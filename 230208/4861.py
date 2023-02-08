T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    word = [input() for _ in range(N)]
    cnt = []

    # 가로
    for i in range(N):
        for j in range(N-M+1):
            w1 = ''
            for k in range(M):
                w1 += word[i][j+k]
            if w1 == w1[::-1]:
                cnt.append(w1)

    # 세로
    for j in range(N):
        for i in range(N-M+1):
            w2 = ''
            for k in range(M):
                w2 += word[i+k][j]
            if w2 == w2[::-1]:
                cnt.append(w2)

    print(f'#{tc}', *cnt)


