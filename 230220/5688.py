T = int(input())
lst = []

for i in range(10**6+1):
    lst.append(i**3)


for tc in range(1, T+1):
    N = int(input())
    if N in lst:
        print(f'#{tc} {lst.index(N)}')
        continue
    else:
        print(f'#{tc} -1')