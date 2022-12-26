import sys
from collections import deque

matrix = [[sys.stdin.readline().rstrip()] for _ in range(6)]

dx, dy = [-1, 1, 0, 0],[0, 0, 1, -1]
visited = []



def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    selected = []
    if a == 0:
        selected.append
