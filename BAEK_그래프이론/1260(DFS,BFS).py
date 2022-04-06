import sys

n,m,v = map(int,sys.stdin.readline().split())
graph = {}

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if a not in graph.keys():
        graph[a] = set([b])
    else:
        graph[a].add(b)
    if b not in graph.keys():
        graph[b] = set([a])
    else:
        graph[b].add(a)
print(graph)