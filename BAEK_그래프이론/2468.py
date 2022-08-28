import sys
from collections import deque

n = int(input())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
cnt = 0 
highest_area = 0
for i in range(n):
    for j in range(n):
        highest_area = max(highest_area, matrix[i][j])

def bfs(x, y, a):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:
                if matrix[nx][ny] > a:
                    bfs(nx, ny, a)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i, j, 4)
            cnt += 1
print(cnt)