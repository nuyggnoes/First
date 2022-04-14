import sys

n, m = map(int,sys.stdin.readline().split())
g = {}

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if a not in g.keys():
        g[a] = set([b])
    else:
        g[a].add(b)
    if b not in g.keys():
        g[b] = set([a])
    else:
        g[b].add(a)
print(g)