from re import T


def DFS(graph,root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                t = list(set(graph[n])-set(visited))
                t.sort(reverse=True)
                stack += t
    return ' '.join(str(i) for i in visited)

n,m,v = map(int,input().split())
graph = {}

for _ in range(m):
    a,b = map(int,input().split())
    if a not in graph.keys():
        graph[a] = set([b])
    else:
        graph[a].add(b)
    if b not in graph.keys():
        graph[b] = set([a])
    else:
        graph[b].add(a)
print(DFS(graph,v))