import sys
input = sys.stdin.readline
info = []
for i in range(int(input())):
    info.append(list(map(str,input().split())))
    info[i][0] = int(info[i][0])
info.sort(key=lambda x : x[0])
for i in info:
    print(i[0],i[1])