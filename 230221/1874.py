N = int(input())
lst = list(range(8, 0, -1))
ST = []
p = []

for i in range(N):
    num = int(input())
    if not ST:
        for _ in range(num):
            ST.append(lst.pop())
            p.append('+')

    elif ST[-1] < num:
        while ST[-1] != num:
            ST.append(lst.pop())
            p.append('+')


    elif ST[-1] > num:
        while ST[-1] != num:
            v = ST.pop()
            p.append('-')
            lst.append(v)

    if ST[-1] == num:
        ST.pop()
        p.append('-')


print(p)
