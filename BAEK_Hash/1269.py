import sys

a,b = map(int,sys.stdin.readline().split())

a1 = set(map(int,sys.stdin.readline().split()))
b1 = set(map(int,sys.stdin.readline().split()))
result = (a1 - b1) | (b1 - a1)
print(len(result))