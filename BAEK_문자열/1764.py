import sys

n,m = map(int,sys.stdin.readline().split())
list_n = []
list_m = []

for i in range(n):
    list_n.append(sys.stdin.readline().rstrip())
for i in range(m):
    list_m.append(sys.stdin.readline().rstrip())

s1 = set(list_n)
s2 = set(list_m)
result = list(s1 & s2)
result.sort()

print(len(result))
for i in result:
    print(i)