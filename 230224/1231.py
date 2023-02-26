def inorder(root):
    global word
    if root<=N:
        inorder(root*2)
        word += lst[root]
        inorder(root*2+1)
    return word



for tc in range(1, 10+1):
    N = int(input())
    lst = [0]*(N+1)
    word = ''

    for _ in range(N):
        p = list(input().split())
        lst[int(p[0])] = p[1]

    print(f'#{tc} {inorder(1)}')