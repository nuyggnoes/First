import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    i = list(map(str,sys.stdin.readline().split()))
    lst.append(i)
lst.sort(key = lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in lst:
    print(i[0])