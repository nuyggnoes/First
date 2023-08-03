import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
number = deque(range(1, n+1))
queue = []

while(number):
    for _ in range(k-1):
        number.append(number.popleft())
    queue.append(number.popleft())
print('<'+', '.join(map(str,queue))+'>')