T = int(input())
for tc in range(1, T + 1):
    A, B = map(str, input().split())  # 전체, 구하고자하는것
    N = len(A)
    M = len(B)

    i = 0
    cnt = 0
    while i < N-M+1:
        if A[i:i+M] != B:
            i += 1
        else:
            cnt += 1
            i += M
    print(f'#{tc} {N-(M-1)*cnt}')


def find(T, P):
    lenT = len(T)
    lenP = len(P)
    idxT = 0
    cnt = 0
    while idxT < lenT-lenP + 1:
        idxP = 0
        while idxP<lenP and T[idxT+idxP] == P[idxP]:
            idxP += 1
        if idxP==lenP:
            cnt += 1
            idxT += lenP
        else:
            idxT += 1
    return cnt