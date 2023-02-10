T = int(input())

for tc in range(1, T + 1):
    word = input()
    inp1 = '..#..'
    inp2 = '.#.#.'
    f1 = ''
    f2 = ''
    f3 = ''

    for i in range(len(word)):
        if i < len(word)-1:
            f1 += inp1[:4]
        if i == len(word)-1:
            f1 += inp1

    for i in range(len(word)):
        if i < len(word)-1:
            f2 += inp2[:4]
        if i == len(word)-1:
            f2 += inp2

    for i in range(len(word)):
        newinp = f'#.{word[i]}.#'
        if i < len(word)-1:
            f3 += newinp[:4]
        if i == len(word)-1:
            f3 += newinp

    print(f1)
    print(f2)
    print(f3)
    print(f2)
    print(f1)




