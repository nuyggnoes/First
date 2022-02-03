import sys


import sys
n = int(sys.stdin.readline())
queue = []
for i in range(n):
    l = sys.stdin.readline().split()
    if l[0] == 'push':
        queue.append(l[1])

    elif l[0] == 'pop':
        if not queue : print('-1')
        else : 
            print(queue[0])
            queue = queue[1:]
    
    elif l[0] == 'size':
        print(len(queue))
    
    elif l[0] == 'empty':
        if not queue : print('1')
        else: print('0')
    
    elif l[0] == 'front':
        if not queue : print('-1')
        else : print(queue[0])
    
    elif l[0] == 'back':
        if not queue : print('-1')
        else : print(queue[-1])