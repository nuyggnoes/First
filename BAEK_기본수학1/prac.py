import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}
for i in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    dic[name] = str(i)
    dic[str(i)] = name
print(dic)
