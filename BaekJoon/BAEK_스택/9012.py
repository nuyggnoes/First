import sys
t = int(sys.stdin.readline())
for i in range(t):
    l = sys.stdin.readline()
    stack = []
    for i in l:
        if i == '(':
            stack.append(i)
        elif i == ')' and '(' not in stack:
            stack.append(i)
        elif i == ')':
            stack.pop()
    if stack == []: print("YES")
    else : print("NO")