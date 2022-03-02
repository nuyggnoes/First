import sys

n = list(sys.stdin.readline().rstrip())
stack = []

for i in range(len(n)):
    if n[i] == '-':
        if stack:
            stack.pop()
            n.insert(i,')')
        else:
            n.insert(i+1,'(')
            stack.append('(')
if stack : n.append(')')

