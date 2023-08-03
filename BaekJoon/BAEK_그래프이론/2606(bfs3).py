from collections import deque
n=int(input())
v=int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(v):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1]=1
Q = [1]

while Q:
    m=Q.pop(0)
    for i in graph[m]:
        if visited[i] == 0:
            Q.append(i)
            visited[i] = 1

print(sum(visited)-1)