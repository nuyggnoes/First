import sys
n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline().rstrip()
    b = list(a.split())
    b.reverse()
    print('Case #%d:'%(i+1),end = ' ')
    print(' '.join(b))