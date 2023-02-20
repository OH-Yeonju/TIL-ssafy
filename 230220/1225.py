for _ in range(10):
    tc = int(input())
    lst = list(map(int, input().split()))

    no = 1
    while lst:
        v = lst.pop(0)
        v = v - no
        if v <= 0:
            v = 0
            lst.append(v)
            break
        lst.append(v)
        no = no+1
        if no > 5:
            no = no-5
    print(f'#{tc}', *lst)