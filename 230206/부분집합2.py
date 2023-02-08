# for n in range(0, 2**N)
N = 3 # 원소개수 = 비트수
ARR = [10, 20, 30]
for n in range(0, 1<<N): # 1을 왼쪽으로 N번 쉬프트한 값, n = 전부 부분집합
    for j in range(N):
        r = n & (1<<j)
        if r != 0:
            print(ARR[j], end=' ')
    print()