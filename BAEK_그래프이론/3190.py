import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
ground = [[0 for _ in range(n)] for _ in range(n)]    #ground
for _ in range(k):
    x,y = map(int,sys.stdin.readline().split())       #사과의 위치를 표시
    ground[x-1][y-1] = 'A'
l = int(sys.stdin.readline())
d = []
for _ in range(l):
    d.append(list(map(str,sys.stdin.readline().split())))    #방향 전환 리스트
stack = ''     #방향 전환 저장
tail = []
cnt = 0
move = [(0,0)]     #시작지점

while True:
    nx,ny = move.pop()
    if not stack:
        ny += 1
        move.append((nx,ny))
    else:
        if stack == 'D':
            nx += 1
            move.append(nx,ny)
    cnt += 1
    break
print(nx,ny)