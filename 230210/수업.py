def check(lst):
    confirms = [False] * 10
    for n in lst:
        if confirms[n] == True:
            return 0
        confirms[n] = True
        return 1

    #또는
    confirm = [0]*10
    for n in lst:
        if confirm[n]:
            return 0
        confirm[n] += 1
        return 1

# 스도쿠문제에서..
for i in [0, 3, 6]:
    for j in [0, 3, 6]:
        lst = ARR[i][j:j+3] + ARR[i+1][j:j+3] + ARR[i+2][j:j+3]
        if len(set(lst)) != 9:
            return 0


for i in [0, 3, 6]:
    for j in [0, 3, 6]:
        lst = []
        for r in range(i, i+3):
            for c in range(j, j+3):
                lst.append(ARR[r][c])
        if check(lst)