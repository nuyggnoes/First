import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    xy = list(map(int,sys.stdin.readline().split()))
    li.append(xy)
li.sort()
for i in range(n):
    print(li[i][0], end = ' ')
    print(li[i][1])