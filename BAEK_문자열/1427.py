import sys

n = list(sys.stdin.readline().rstrip())

n.sort()
n.reverse()

print(''.join(n))
