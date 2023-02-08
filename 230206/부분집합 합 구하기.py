TC = int(input())

N = 10

for _ in range(1, TC+1):
    ARR = list(map(int, input().split()))
    for n in range(1<<N):
        sumV = 0
        j_lst = []
        for j in range(N):
            r = n & (1<<j)
            if r != 0:
                j_lst.append(ARR[j])
                sumV += ARR[j]
        if len(j_lst) != 0 and sumV == 0:
            print(j_lst)


