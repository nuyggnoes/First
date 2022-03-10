import sys

n, m = map(int,sys.stdin.readline().split())
start_field = list(map(int,sys.stdin.readline().split()))
sum = [0] * n
x = []
for i in range(m):
    a,b,k = map(int,sys.stdin.readline().split())
    x = start_field[a-1:b]
    x = [i+k for i in x]
    sum[a-1:b] = x
    print(sum)