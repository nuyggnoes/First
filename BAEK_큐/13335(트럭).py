import queue
import sys
from collections import deque
n, w, l = map(int,sys.stdin.readline().split())
truck = deque(map(int,sys.stdin.readline().split()))
queue = []

while True:
    queue.append(truck.popleft())