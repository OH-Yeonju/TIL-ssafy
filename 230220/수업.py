Q = []
no = 1
M = 20
Q.append((no, 1))   # 1번 줄, 마이쮸1개
total = 0

while Q:
    print(Q)
    curNo, curMychu = Q.pop(0)  # 1번 받아감
    total += curMychu
    print(curNo, curMychu, total)
    if total >= M:
        break
    Q.append((curNo, curMychu+1))   # 1번 줄, 마이쭈 2개
    no += 1
    Q.append((no, 1))   # 2번 줄, 마이쭈 1개

# curNo, curMychu = Q.pop(0)  # 1번 받아감
# Q.append(curNo)   # 1번 줄
# no += 1
# Q.append(no)



