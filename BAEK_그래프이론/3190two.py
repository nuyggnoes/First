from collections import deque
import sys

n = int(sys.stdin.readline())
ground = [[0] * n for _ in range(n)]

for _ in range(int(sys.stdin.readline())):         #사과위치 저장
    a,b = map(int,sys.stdin.readline().split())
    ground[a-1][b-1] = 1

change = {}
k = int(sys.stdin.readline()) 
for _ in range(k):                                 #방향 변경 정보 저장
    x,c = map(str,sys.stdin.readline().split())
    change[int(x)] = c

snake = deque([(0,0)])

dx,dy = [-1,0,1,0],[0,1,0,-1]

d = 1
t = 0
nx, ny = 0, 0

def ground_check(x,y):             #ground 범위 체크 함수
    return True if 0 <= x < n and 0 <= y < n else False

def change_direction(direction):    #방향 전환 함수
    global d
    if direction == 'D':
        d = (d+1)%4
    else:
        d = (d-1)%4
    return d

while True:
    t += 1
    nx = nx + dx[d]
    ny = ny + dy[d]

    if t in change.keys():          #방향 전환
        d = change_direction(change[t])
    
    if ground_check(nx,ny):
        if (nx,ny) in snake:      #몸과 충돌
            break

        if ground[nx][ny] == 1:
            ground[nx][ny] = 0
            snake.append((nx,ny))
        
        elif ground[nx][ny] == 0:
            snake.append((nx,ny))
            snake.popleft()
    else:
        break

print(t)