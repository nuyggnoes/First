import sys

graph = {}
n = int(sys.stdin.readline())
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)

def DFS(graph):
    visited = []
    stack = [1]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph.keys():
                temp = list(set(graph[n])-set(visited))
                temp.sort(reverse=True)
                stack += temp
    return len(visited) - 1
print(DFS(graph))