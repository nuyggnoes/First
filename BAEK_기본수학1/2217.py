import sys

n = int(sys.stdin.readline())
r = []
ans = []

for _ in range(n):
    r.append(int(sys.stdin.readline()))
r.sort()

for i in range(1, n+1):
    w = i * r[-1 - (i-1)]
    ans.append(w)

print(max(ans))