X = int(input())

num1 = 0
num2 = 0
cnt = 0
while cnt <= 10000000:
    if num1 == 0 and num2 == 0:
        num1 += 1
        num2 += 1
        cnt += 1
    if num1 == 1:
        num2 += 1
        cnt += 1
        continue
    if num1 == num2:
        num2 += 1
        num1 -= 1
        cnt += 1
    if num1 < num2:
        num2 -= 1
        num1 += 1
        cnt += 1
    if num1 > num2:
        num1 -= 1
        num2 += 1
        cnt += 1
    if cnt == X:
        break
print(f'{num1} / {num2}')
