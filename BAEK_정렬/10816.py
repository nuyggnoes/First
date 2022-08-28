import sys
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

count = {}
for i in N:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in M:
    result = count.get(i)
    # if result == None:
    #     print(0,end = ' ')
    # else:
    #     print(result, end = ' ')
    print(result,end=' ')
