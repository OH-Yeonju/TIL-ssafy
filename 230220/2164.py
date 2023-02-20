from collections import deque
N = int(input())

lst = deque(range(1, N+1))

while len(lst) > 1:
    lst.popleft()
    v = lst.popleft()
    lst.append(v)

print(*lst)