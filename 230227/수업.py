dV = 10
# print(dV, bin(dV), hex(dV))


def decTobin(value):   # 십진수를 이진수로(숫자들어옴)
    s = ''
    for j in range(3, -1, -1):
        s += '1' if value & (1<<j) else '0'
    print(s)
        # r = value & (1<<j)
        # if r!=0:
        #     print(1)
        # else:
        #     print(0)

decTobin(10)


def hextodec(s):     # 16진수를 십진수로(문자들어옴)
    if s.isdigit():
        return int(s)
    else:
        return ord(s) - ord('A') + 10

print(hextodec('A'))


def hextobin(s):
    # 16진수를 10진수로
    if s.isdigit():
        decV = int(s)

    else:
        decV = ord(s) - ord('A') + 10

    # 10진수를 2진수로
    res = ''
    for j in range(3, -1, -1):
        res += '1' if decV & (1<<j) else '0'

    return res

print(hextobin('F'))
print(hextobin('A'))
print(hextobin('5'))


def hecTobin(s):
    mapping = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
               '4':'0100', '5':'0101', '6':'0110', '7':'0111',
               '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
               'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    return mapping[s]

# '7329'
def atoi(s):
    res = 0
    for n in s:
        value = int(n)
        res = res*10 + value
    return res



def bintodec(s):
    res = 0


def bintohex(s):
    resD = 0
    for n in s:
        value = int(n)
        resD = resD*2 + value
    if resD < 10:
        return str(resD)
    else:
        return str((resD-10) + ord('A'))
