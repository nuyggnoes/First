import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    li.append(list(map(str,sys.stdin.readline().split())))
    li[i][0] = int(li[i][0])

li.sort(key = lambda x : x[0])

for i in li:
    print(i[0],i[1])