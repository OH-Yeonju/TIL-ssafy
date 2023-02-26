def inorder(rootIdx):
    global cnt
    if rootIdx<=N:
        inorder(rootIdx*2)
        lst[rootIdx] = cnt
        cnt += 1
        inorder(rootIdx*2+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    cnt = 1
    inorder(1)
    print(f'#{tc} {lst[1]} {lst[N//2]}')
