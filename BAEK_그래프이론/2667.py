from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

def BFS(graph, a, b):            #BFS 이용
    n = len(graph)
    queue = deque() 
    queue.append((a,b))      
    graph[a][b] = 0         
    count = 1                 

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:       
                graph[nx][ny] = 0        
                queue.append((nx,ny))    
                count += 1
    return count

n = int(input())
ground = []
for _ in range(n):
    ground.append(list(map(int,input())))

cnt = []
for i in range(n):
    for j in range(n):
        if ground[i][j] == 1:
            cnt.append(BFS(ground, i, j))
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)