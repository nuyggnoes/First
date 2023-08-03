import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
cnt, cnt_color_weekness = 0,0

def search(x, y):
    visited[x][y] = True
    current_color = matrix[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:         #방문을 하지 않았고
                if matrix[nx][ny] == current_color:   #현재의 색과 같으면
                    search(nx, ny)                #search 함수를 호출하여 같은 색깔의 방문을 True로 바꿔줌

for i in range(n):                 #일반인 기준 영역 개수 구하기
    for j in range(n):
        if visited[i][j] == False:
            search(i, j)
            cnt += 1

for i in range(n):               #R과 G를 구분할 수 없음
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

visited = [[False] * n for _ in range(n)]   #방문 초기화

for i in range(n):                #적록색약의 영역 개수 구하기
    for j in range(n):
        if visited[i][j] == False:
            search(i, j)
            cnt_color_weekness += 1

print(cnt, cnt_color_weekness)