import sys

while True:
    l = sys.stdin.readline().rstrip()
    flag = True
    stack = []
    if l == '.': break
    for i in l:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack and stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack and stack[-1] == '[':
                stack.pop()
    if stack or flag == False:
        print('no')
    elif not stack  or flag == True:
        print('yes')