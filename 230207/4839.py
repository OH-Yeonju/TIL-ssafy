def binary_cnt(key):
    s = 1
    e = P
    cnt = 0
    while s <= e:
        m = int((s+e)/2)
        cnt += 1
        if m < key:
            s = m
        else:
            e = m
        if m == key:
            return cnt
    return cnt


T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    if binary_cnt(A) < binary_cnt(B):
        print(f'#{tc} A')
    elif binary_cnt(A) > binary_cnt(B):
        print(f'#{tc} B')
    else:
        print(f'#{tc} {0}')