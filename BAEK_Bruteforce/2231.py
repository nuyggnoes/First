import sys
n = int(sys.stdin.readline())
result = 0
for i in range(1,n):
    if i + sum(map(int, str(i))) == n : 
        result = i
        break
print(result)