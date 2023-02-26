def insert(item):
    pos = 1
    while TREE[pos] != 0:
        if TREE[pos] == item:
            return
        if TREE[pos] < item:
            pos = pos*2 + 1
        else:
            pos = pos*2
    TREE[pos] = item

def find(key):
    pos = 1
    while TREE[pos] != 0:
        if TREE[pos] == key:
            return pos
        if TREE[pos] < key:
            pos = pos*2 + 1
        else:
            pos = pos*2
    return -1



lst = [9, 4, 12, 3, 6, 15, 13, 17]
TREE = [0] * 100
for item in lst:
    insert(item)
    print(TREE)


insert(5)
print(TREE)
print(find(12))
print(find(17))
print(find(3))
print(find(2))
print(find(20))
print(find(7))