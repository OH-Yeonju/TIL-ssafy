def push(item):
    stack.append(item)

def pop():
    if len(stack) > 0:
        return stack.pop(-1)  # 이거만 쓰면 데이터가 없을 때 써버리면 오류가 남
    return -1


def push(item):
    global top   # 글로벌 변수 사용

    if top == SIZE-1:
        print('overflow')
        return -1

    top += 1
    stack[top] = item
    return 1


def peek():
    if top == -1:
        return -1
    return stack[top]



def pop():
    global top

    if top == -1:
        print('underflow')
        return -1

    t = stack[top]
    top -= 1
    return t

def isEmpty():
    if top == -1:
        return True
    else:
        return False


def isFull():
    if top == SIZE-1:
        return True
    else:
        return False


SIZE = 10
stack = [-1]*SIZE  # 빈공간 만들어줌
top = -1         # 아무것도 안들어가있는상태
print(stack)

push('a')
print(stack)

push('b')
print(stack, top)

r = pop()
print(r, stack, top)
r = pop()
r = pop()