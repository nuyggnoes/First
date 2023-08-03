import sys

n = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))
stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append([i, top[i]])
print(" ".join(map(str,result)))