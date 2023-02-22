def preOrder(root):
    print(root)
    if len(TREE[root]):
        preOrder(TREE[root][0])
    if len(TREE[root])==2:
        preOrder(TREE[root][1])


def inOrder(root):
    if len(TREE[root]):
        inOrder(TREE[root][0])
    if len(TREE[root]) == 2:
        inOrder(TREE[root][1])
    print(root)



N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
TREE = [[] for _ in range(N+1)]

for idx in range(0, len(lst), 2):
    p = lst[idx]
    c = lst[idx+1]
    TREE[p].append(c)

# print(TREE)
# preOrder(1)
inOrder(1)