import sys
from collections import deque

t = int(input())
flag = True
stack = []

for _ in range(t):
    stack = []
    flag = True
    p = sys.stdin.readline().rstrip()
    p = p.replace('RR','')
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()
    a = a.replace('[','')
    a = a.replace(']','')
    if a: a = a.split(',')
    a = deque(a)
    for i in range(len(p)):

        if p[i] == 'R' and not stack:
            stack.append(p[i])
            continue
        elif p[i] == 'R' and stack:
            stack.pop()
            continue
        elif p[i] == 'D' and not a:
            flag = False
            break
        elif p[i] == 'D' and not stack:
            a.popleft()
        elif p[i] == 'D' and stack:
            a.pop()
    if stack:
        a.reverse()
    if flag :
        print('[' + ','.join(list(a))+ ']')
    else: print('error')