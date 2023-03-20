from collections import deque
n = int(input())
v = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(v):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            DFS(i)
DFS(1)

print(sum(visited)-1)