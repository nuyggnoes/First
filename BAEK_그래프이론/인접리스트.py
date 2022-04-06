import sys

n, m = map(int,sys.stdin.readline().split())
g = {}

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if a not in g.keys():
        g[a] = [b]
    else:
        g[a].append(b)
    if b not in g.keys():
        g[b] = [a]
    else:
        g[b].append(a)
print(g)