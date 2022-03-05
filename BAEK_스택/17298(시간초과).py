import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().rstrip().split()))
stack = []
ans = []

for i in range(n - 1):
    x = i
    stack.append(a[i])
    if stack[-1] < a[i+1]:
        ans.append(a[i+1])
        stack.pop()
    else:
        if (i+2 == n):
            if stack[-1] < a[i+1]:
                ans.append(a[i+1])
                break
            else:
                ans.append(-1)
        else:
            for x in range(i+2,n):
                if stack[-1] < a[x]:
                    ans.append(a[x])
                    break
                elif x == n-1:
                    ans.append(-1)
ans.append(-1)
print(*ans)