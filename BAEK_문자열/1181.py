import sys
n = int(sys.stdin.readline())
arr = set()
for i in range(n):
    arr.add(sys.stdin.readline().rstrip())
print(arr)
arr = list(arr)
arr.sort()
print(arr)
arr.sort(key=len)

for i in arr:
    print(i)