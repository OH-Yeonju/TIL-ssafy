N = int(input())
lst = list(map(int, input().split()))
s = int(input())

for _ in range(s):
    n1, n2 = map(int, input().split())
    if n1 == 1:
        for i in range(N):
            if (i+1)%n2 == 0:
                if lst[i] == 1:
                    lst[i] = 0
                else:
                    lst[i] = 1
    if n1 == 2:
        for i in range(N):
            if 0<=n2-i<N and 0<=n2+1<N:
                if lst[n2-i] == lst[n2+i]:
                    if lst[n2-i] == 0:
                        lst[n2-i], lst[n2+i] = 1, 1
                    elif lst[n2-1] == 1:
                        lst[n2-i], lst[n2+i] = 0, 0
                else:
                    break
print(lst)