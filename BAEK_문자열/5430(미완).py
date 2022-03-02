import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    cmd = deque([])
    li = deque([])
    cmd.append(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()
    for i in a:
        if i.isdigit():
            li.append(i)
    for i in range(len(cmd)):
        if cmd[i] == 'R':
            li.reverse()
        elif cmd[i] == 'D':
            if not li:
                print('error')
                break
            else:
                li.popleft()
    print(li)