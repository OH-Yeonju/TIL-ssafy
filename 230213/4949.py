# def ispair(sen):
#     stack = []
#     for s in sen:
#         if s == '(' or '[':
#             stack.append(s)
#
#         elif s == ')':
#             if len(stack) == 0:
#                 return 'NO'
#             t = stack.pop(-1)
#             if t != '(':
#                 return 'NO'
#         elif s == ']':
#             if len(stack) == 0:
#                 return 'NO'
#             t = stack.pop(-1)
#             if t != '[':
#                 return'NO'
#     if len(stack) > 0:
#         return 'NO'
#     return 'YES'

def inPair(word):
    stack = []
    for c in word:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 'no'
            t = stack.pop(-1)
            if t != '(':
                return 'no'

        if c == '{':
            stack.append(c)
        elif c == '}':
            if len(stack) == 0:
                return 'no'
            t = stack.pop(-1)
            if t != '{':
                return 'no'

    if len(stack) > 0:
        return 'no'
    return 'yes'


while True:
    sen = input()
    if sen == '.':
        break
    print(inPair(sen))