import sys

n,m = map(int,sys.stdin.readline().split())
idol = {}

for i in range(n):
    group = sys.stdin.readline().rstrip()
    x = int(sys.stdin.readline())
    group_list = []
    for i in range(x):
        group_list.append(sys.stdin.readline().rstrip())
    idol[group] = sorted(group_list)

for i in range(m):
    q = sys.stdin.readline().rstrip()
    p = int(sys.stdin.readline())
