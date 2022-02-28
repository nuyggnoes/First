import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
b = set(arr)
b = list(b)
b.sort()
b.sort(key=len)

for i in b:
    print(i)