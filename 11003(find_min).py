from collections import deque
import sys
input = sys.stdin.readline
N,L = map(int, input().split())
num = list(map(int,input().split()))

q = deque()
answer = []