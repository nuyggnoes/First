import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
tomato_box = []
for i in range(n):
    tomato_box.append(list(map(int,sys.stdin.readline().split())))   #토마토 상자
stack = deque([])
for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            stack.append((i,j))

dx,dy = [-1,1,0,0],[0,0,1,-1]   #방향
day = 0                         #걸린 시간

def bfs():
    while stack:
        x,y = stack.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato_box[nx][ny] == 0:
                tomato_box[nx][ny] = tomato_box[x][y] + 1
                stack.append([nx,ny])

bfs()
for i in tomato_box:
    for j in i:
        if j == 0:
            print(-1)
            break
    day = max(day, max(i))
print(day - 1)