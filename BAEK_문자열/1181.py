import sys
n = int(sys.stdin.readline())
arr = set()
for i in range(n):
    arr.add(sys.stdin.readline().rstrip())
arr = list(arr)
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)