def inOrder(rootIdx):
    if lst[rootIdx]:
        inOrder(rootIdx*2)
        print(lst[rootIdx])
        inOrder(rootIdx*2+1)

def findA(idx):
    while idx//2 >= 1:
        idx = idx//2
        print(lst[idx])




lst = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'] + [0]*100


inOrder(1)