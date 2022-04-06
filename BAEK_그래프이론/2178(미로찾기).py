import sys
from collections import deque

n,m = map(int,input().split())
miro = [input() for _ in range(n)]     #미로
visited = [[0 for _ in range(m)] for _ in range(n)]      #방문경로
dx,dy = [-1,1,0,0], [0,0,-1,1]    #방향

queue = deque([(0,0)])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    if x == n - 1 and y == m - 1:
        print(visited[x][y])
        break

    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]

        if 0 <= ax < n and 0 <= ay < m:
            if visited[ax][ay] == 0 and miro[ax][ay] == '1':
                visited[ax][ay] = visited[x][y] + 1
                queue.append((ax,ay))