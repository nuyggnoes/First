import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
stack = []

for i in a:
    for j in a:
        if i < j:
            stack.append(j)
            a = a[1:]
            break
        elif j == a[len(a)-1]:
            stack.append(-1)
            a = a[1:]
for i in stack:
    print(i, end = ' ')