def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1<<j) else '0'
    print(output)

for i in range(-5, 6):
    print('%3d = ' %i, end='')
    Bbit_print(i)



def Bbit_print2(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1<<j) else '0'
    print(output, end=' ')
a = 0x10
x = 0x01020304
print('%d = ' %a, end='')
Bbit_print2(a)
print()
print('0%X = '%x, end='')
for i in range(0, 4):
    Bbit_print2((x>>i*8) & 0xff)



def ce(n): # change endian
    p = []
    for i in range(0, 4):
        p.append((n>>(24 -i*8)) & 0xff)
    return p

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x>>(i*8)) & 0xff)
print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
p = ce(x)
print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))


def ce1(n):
    return (n<<24&0xff000000) | (n<<8 & 0xff0000) | (n>> 8 &0xff00) | (n>>24&0xff)

# def Bbit_print3(i):
#     output = ''
#     for j in range(7, -1, -1):
#         output += '1' if i & (1<<j) else '0'
#     print(output)
#
# a = 0x86
