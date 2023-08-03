from collections import deque
n = int(input())
v = int(input())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
for i in range(v):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
dq = deque([1])

while dq:    #bfs
    m = dq.popleft()
    for x in graph[m]:
        if visited[x] == 0:
            dq.append(x)
            visited[x] = 1
print(sum(visited)-1)