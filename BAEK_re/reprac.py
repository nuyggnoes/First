import sys
input = sys.stdin.readline
N = int(input())
n = list(map(int,input().split()))
n.sort()
M = int(input())
m = list(map(int,input().split()))
m.sort()
print(n,m)
# for i in m:
#     if i in n:
#         print(1)
#     else:
#         print(0)