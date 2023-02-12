import sys
input = sys.stdin.readline
T = int(input())
while T>0:
    l = list(map(int,input().split()))
    sum = 0
    av = 0
    cnt = 0
    for i in range(1,len(l)):
        sum += l[i]
        av = sum/(len(l)-1)
    for i in range(1,len(l)):
        if l[i] > av:
            cnt += 1
    result = cnt/(len(l)-1)*100
    print(format(result, ".3f"),end="%")
    print("")
    T-=1