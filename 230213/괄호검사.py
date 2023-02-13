# input_s = '( )( )((( )))'
# input_s = '((( )((((( )( )((( )( ))((( ))))))'
# input_s = '())'
# input_s = '(()'

# 짝이 맞으면 True, 아니면 False를 return 합니다
def inPair(input_s):
    stack = []
    for c in input_s:
        if c == '(':      # 왼쪽 괄호면 스택에 넣어주고
            stack.append(c)
        elif c == ')':    # 짝이 되는 오른쪽 괄호가 나왔을 때
            if len(stack) == 0:  # 스택에 아무것도 안 들었을 경우
                return False

            t = stack.pop(-1)
            if t != '(':
                return False
    if len(stack) > 0:  # 반복문 다 돌았는데 남아있는 경우
        return False
    return True  # 이 모든 경우가 아니면

print(inPair(input_s))