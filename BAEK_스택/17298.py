import sys
input = sys.stdin.readline
n = int(input())
number = list(map(int,input().split()))
ans = [-1] * n
stack = []
max = -1
