import sys

n = int(sys.stdin.readline())
lst = sorted(list(map(int,sys.stdin.readline().split())))
result = []
m = 1000000
for i in range(n-1):
    for j in range(i+1,n):
        sum = lst[i] + lst[j]
        if abs(sum) > abs(m):
            continue
        else:
            m = sum
            result.clear()
            result.append(lst[i])
            result.append(lst[j])
print(result[0], result[1])