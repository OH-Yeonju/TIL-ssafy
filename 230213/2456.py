N = int(input())
a_lst = [0]*3
b_lst = [0]*3
c_lst = [0]*3
a_sum = 0
b_sum = 0
c_sum = 0

for _ in range(N):
    A, B, C = map(int, input().split())
    a_lst[A-1] += 1
    a_sum += A
    b_lst[B-1] += 1
    b_sum += B
    c_lst[C-1] += 1
    c_sum += C

print(a_lst, a_sum)
print(b_lst, b_sum)
print(c_lst, c_sum)