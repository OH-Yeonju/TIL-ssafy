# import heapq
#
# h = []
# lst = [15, 4, 13, 20, 11, 19]
# for item in lst:
#     heapq.heappush(h, item)
#
#
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))


# 최대힙,, 최소힙일때는 c p 비교 부등호만 바꿔주면 됨
def enq(item):
    global last
    last += 1
    TREE[last] = item
    c = last
    p = c//2
    while p>=1 and TREE[c] > TREE[p]:  # 힙이 깨졌으면
        TREE[c], TREE[p] = TREE[p], TREE[c]
        c = p
        p = c//2


# 최대힙일시,, 최소힙일 경우 if의 비교부분 바꿔줌
def deq():
    global last
    tmp = TREE[1]
    TREE[1] = TREE[last]
    last -= 1
    p = 1
    c = p*2
    while c<=last:     # p가 자식노드가 하나라도 있는 동안
        if c+1<=last and TREE[c]<TREE[c+1]:   #오른쪽 자식노드가 있으면 and 오른쪽 노드가 더 크면:
            c += 1
        if TREE[p] < TREE[c]:   # heap이 깨졌으면
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p*2
        else:
            break    # 힙이 안깨졌을땐 그대로 빠져나옴

    return tmp





TREE = [0] * 100
last = 0
lst = [15, 4, 13, 20, 11, 19]
for item in lst:
    enq(item)
    print(TREE)

enq(23)
print(TREE)

print(deq())
print(last, TREE)
print(deq())
print(last, TREE)
print(deq())
print(last, TREE)