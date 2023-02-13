def po(A, B):
    if B == 1:
        return A
    return A * po(A, B-1)


for tc in range(1, 10+1):
    N = int(input())
    A, B = map(int, input().split())
    print(f'#{tc} {po(A, B)}')
