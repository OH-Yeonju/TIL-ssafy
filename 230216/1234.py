for tc in range(1, 10+1):
    N, word = input().split()
    ST = []
    for i in word:
        if ST and ST[-1] == i:
            ST.pop()
            continue
        ST.append(i)

    print(f'#{tc}', ''.join(ST))