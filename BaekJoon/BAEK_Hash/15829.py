import sys

l = int(sys.stdin.readline())
li = list(sys.stdin.readline().rstrip())
result = []
for i in range(l):
    result.append((ord(li[i])-96)*(31**i))

print(sum(result))