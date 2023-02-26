# def findA(N):
#     global cnt
#     if c1[N] != 0:
#         cnt += 1
#         findA(c1[N])
#     if c2[N] != 0:
#         cnt += 1
#         findA(c2[N])
#     return

def preorder(root):
    global cnt
    if root:
        preorder(c1[root])
        cnt += 1
        preorder(c2[root])
    return cnt


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    c1 = [0]*(E+2)
    c2 = [0]*(E+2)
    pa = [0]*(E+2)
    for i in range(E):
        p = lst[2*i]
        c = lst[2*i+1]
        pa[c] = p
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    # findA(N)
    # print(f'#{tc} {cnt+1}')
    preorder(N)
    print(f'#{tc} {cnt}')

