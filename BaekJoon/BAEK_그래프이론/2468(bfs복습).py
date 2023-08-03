from collections import deque

n = int(input())
matrix = []
highest_area = 0

for i in range(n):
    matrix.append(list(map(int,input().split())))
    for j in range(n):
        if matrix[i][j] > highest_area:
            highest_area = matrix[i][j]

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

def bfs(a,b,h,visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] > h and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

result = 0

for i in range(highest_area):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    
    for j in range(n):
        for k in range(n):
            if matrix[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i,visited)
                cnt+=1
    if result < cnt:
        result = cnt
print(result)