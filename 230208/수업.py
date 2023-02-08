# '123'
# i = 1
# i = i*10 + 2
# i = i*10 + 3
# ord() > 문자의 ASCII값을 돌려준다
# chr() > ASCII값에 해당하는 문자를 돌려준다

# i = 0
# for num in '123':
#     i = i*10 + ord(num) - ord('0')
# print(i, type(i))

def itoa(num):
    isMinus = False
    if num<0:
        isMinus = True
        num *= (-1)
    s = ''
    while num>0:
        asc = (num%10) + ord('0')
        num = num//10
        s = chr(asc) + s
    # s = '3'
    # s = '2' + s
    # s = '1' + s
        return s

print(itoa(123))

