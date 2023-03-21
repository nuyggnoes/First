n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
visited = [0]*(n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# def dfs(v):
#     visited[v] = 1
#     for i in graph[v]:
#         if visited[i] == 0:
#             dfs(i)

def bfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1


for i in range(1,n+1):
    if visited[i] == 0:
        cnt += 1
        bfs(i)

print(cnt)