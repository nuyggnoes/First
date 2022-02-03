import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    q = sys.stdin.readline().strip()

    if q[0] == 'push':
        stack.append(q[1])


    elif q[0] == 'pop':
        if not stack : print('-1')
        else :
            print(stack.pop())

    elif q[0] == 'size':
        print(len(stack))

    elif q[0] == 'empty':
        if not stack: print('1')
        else: print('0')

    elif q[0] == 'top':
        if not stack : print('-1')
        else:
            print(stack[-1])