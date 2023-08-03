from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

def bfs(graph, a, b):
    stack = deque()
    stack.append((a,b))
    graph[a][b] = 0
    count = 1

    while stack:
        x,y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append((nx,ny))
                count += 1
    return count

def result():
    global m,n,k
    m, n, k = map(int,input().split())
    ground = [[0] * m for _ in range(n)]

    for _ in range(k): 
        i,j = map(int,input().split())
        ground[j][i] = 1

    cnt = []
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                cnt.append(bfs(ground,i,j))
    return len(cnt)

test_case = int(input())
for _ in range(test_case):
    print(result())