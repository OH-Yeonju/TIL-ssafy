def inOrder(rootIdx):
    if word[rootIdx]:
        inOrder(rootIdx*2)
        p.append(word[rootIdx])
        inOrder(rootIdx*2+1)


for tc in range(1, 10+1):
    N = int(input())
    word = [0]
    for _ in range(N):
        lst = list(input().split())
        word.append(lst[1])

    word = word + [0]*100
    p = []
    inOrder(1)
    print(f'#{tc}', ''.join(p))