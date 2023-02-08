# 행 우선 순회
for i in range(N): # i 행의 좌표
    for j in range(M): # j 열의 좌표
        Array[i][j] # 필요한 연산 수행

# 열 우선 순회
for j in range(M):
    for i in range(N):
        Array[i][j]

# 지그재그 순회
for i in range(N):
    for j in range(M):
        Array[i][j + (M-1-2*j) * (1%2)]

# 델타를 이용한~
# NxN배열
# di[] > [0, 0, -1, 1] < 좌우상하
# dj[] > [-1, 1, 0, 0] < 문제에서 요구하는 순서에 맞게... 숫자를 넣어준다

# 첫번째방법
di = [0, 1, 0, -1] # > 오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]
N = 3
for i in range(N):
    for j in range(N):
        for k in range(4):  # 주변 4방향으로
            ni, nj = i+di[k], j+di[k]
            if 0<=ni<N and 0<=nj<N:
                print(i, j, ni, nj)

# 두번째방법
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                print(i, j, ni, nj)

# 대각선 방향일때도 가능!

# 1칸, 2칸이 아닌 임의의 수(P)일때
di = [0, 1, 0, -1] # > 오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]
N = 3
P = 3
for i in range(N):
    for j in range(N):
        for k in range(4)
            for l in range(1 , P+1):
                ni = i+di[k]*l
                nj = j+di[k]*l
                if 0 <= ni < N and 0 <= nj < N:
                    print(i, j, ni, nj)

# 전치 행렬
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


# 부분집합 합
# 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 ㅂ아법
A = [1, 2, 3, 4]
bit = [0, 0, 0, 0] # [0]*4 있으면 1 없으면 0표시하기 위해서 만듦
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # 이 위까지 부분집합 모두 구한것
                # 합을 구하려면
                s = 0
                for p in range(4):
                    if bit[p]:
                        print(A[P], end=' ')
                        s += A[P]
                print(s)

# 좀 더 간결하게 생성하는 방법
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)  # n = 원소의 개수
for i in range(1<<n):  # 1<< n 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교
        if i & (1<<j):  # i의 j번 비트가 1인 경우
            print(arr[j], end=', ')  # j번 원소 출력
    print()
print()