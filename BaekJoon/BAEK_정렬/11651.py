import sys

n = int(sys.stdin.readline())
cdn = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

cdn.sort(key = lambda x: (x[1],x[0]))

for i in cdn:
    print(i[0],i[1])