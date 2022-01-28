n = int(input())
stack = []
count = 0
for i in range(n):
    q = input().split()

    if q[0] == 'push':
        stack.append(q[1])
        count += 1

    elif q[0] == 'pop':
        if not stack : print('-1')
        else :
            print(stack.pop())
            count -= 1

    elif q[0] == 'size':
        print(count)

    elif q[0] == 'empty':
        if not stack: print('1')
        else: print('0')

    elif q[0] == 'top':
        if not stack : print('-1')
        else:
            print(stack[-1])