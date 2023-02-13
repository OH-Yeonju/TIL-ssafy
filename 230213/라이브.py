stack = [0] * 3
top = -1

top += 1    # push(10)
stack[top] = 10

top += 1    # push(20)
stack[top] = 20

top += 1    # push(30)
stack[top] = 30

if top > -1: # top이 -1일 때 실제로 삭제된게 아니기 때문에 30이 나올 수 있음
    top -= 1
    print(stack[top+1])
if top > -1:
    top -= 1
    print(stack[top+1])
if top > -1:
    top -= 1
    print(stack[top+1])
