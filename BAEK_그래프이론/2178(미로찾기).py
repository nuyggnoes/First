from collections import deque

N,M = map(int,input().split())
miro = [input() for _ in range(N)]   #미로
visited = [[0 for _ in range(M)] for _ in range(N)]    #방문 경로
dx,dy = [-1,1,0,0], [0,0,-1,1]    #방향

queue = deque([(0,0)])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == N - 1 and y == M - 1:    #도착지점에 도착하면 
        print(visited[x][y])        #칸 수를 프린트
        break
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < N and 0 <= ay < M :
            if visited[ax][ay] == 0 and miro[ax][ay] == '1':
                visited[ax][ay] = visited[x][y] + 1
                queue.append((ax,ay))