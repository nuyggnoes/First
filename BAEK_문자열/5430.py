import sys

t = int(sys.stdin.readline())
flag = True

for _ in range(t):
    flag = True
    li = []
    cmd = sys.stdin.readline().rstrip()
    cmd = cmd.replace('RR','')
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().rstrip()
    a = a[1:]
    a = a[:-1]
    if a : li = a.split(',')
    
    for i in range(len(cmd)):
        if cmd[i] == 'R':
            if not li:
                flag = False
                break
            else:
                li = li[::-1]
        elif cmd[i] == 'D':
            if not li:
                flag = False
                break
            else:
                li = li[1:]
    if flag : print('['+','.join(list(li))+']')
    else : print('error')