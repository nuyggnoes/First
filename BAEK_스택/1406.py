import sys

l = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
stack = []
n = len(l)
for _ in range(m):
    ord = sys.stdin.readline().split()
    if ord[0] == 'P':
        l.append(ord[1])
    elif ord[0] == 'L' and l:
        stack.append(l.pop())
    elif ord[0] == 'D' and stack:
        l.append(stack.pop())
    elif ord[0] == 'B' and l:
        l.pop()
stack.reverse()
print(''.join(l+stack))