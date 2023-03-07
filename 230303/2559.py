N, K = map(int, input().split())
lst = list(map(int, input().split()))

resV = []
for i in range(N-K):
    resV.append(sum(lst[i:i+K]))
print(max(resV))