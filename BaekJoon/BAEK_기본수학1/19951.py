import sys

n, m = map(int,sys.stdin.readline().split())
start_field = list(map(int,sys.stdin.readline().split()))
sum = [0] * n

for i in range(m):
    a,b,k = map(int,sys.stdin.readline().split())
    for i in range(a-1,b):
        sum[i] += k

ans = [start_field[i] + sum[i] for i in range(n)]
print(*ans)