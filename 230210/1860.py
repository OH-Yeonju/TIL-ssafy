# 누적 구하는 함수
def bocnt(sec):
    cnt = sec//M * K
    return cnt

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    come = list(map(int, input().split()))

    for i in range(len(come)-1, -1, -1):
        for j in range(i):
            if come[j] > come[j+1]:
                come[j], come[j+1] = come[j+1], come[j]


    peo = 0
    for i in come:
        if bocnt(i) - peo > 0:
            peo += 1
            if peo == len(come):
                print(f'#{tc} possible')
        else:
            print(f'#{tc} impossible')
            break