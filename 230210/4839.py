def binary(key):
    s = 1
    e = P
    cnt = 0

    while s <= e:
        mi = int((s+e)/2)
        cnt += 1
        if mi < key:
            s = mi
        if mi > key:
            e = mi
        if mi == key:
            return cnt


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    if binary(A) > binary(B):
        print(f'#{tc} B')
    if binary(A) < binary(B):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')