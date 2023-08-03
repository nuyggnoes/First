import sys
n = []
for _ in range(int(sys.stdin.readline())):
    n.append(int(sys.stdin.readline()))
n.sort()
for i in n:
    print(i)