def preOrder(root):
    if root:   # 0으로 차있어서 체크가능할때만
        print(root)
    # if leftC[root]:
        preOrder(leftC[root])
    # if rightC[root]:
        preOrder(rightC[root])


def findA(c):
    while c != 0:
        print(parent[c])
        c = parent[c]




N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))

leftC = [0] * (N+1)
rightC = [0] * (N+1)
parent = [0] * (N+1)

for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]

    parent[c] = p
    if leftC[p] == 0:
        leftC[p] = c
    else:
        rightC[p] = c

print(leftC)
print(rightC)
print(parent)

# preOrder(1)

findA(10)