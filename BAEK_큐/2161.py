import sys
from collections import deque
n = int(sys.stdin.readline())
queue = []
number = deque(range(1,n+1))
while n > 1 :
    queue.append(number.popleft())
    number.append(number.popleft())
    n -= 1
queue.append(number.pop())

for i in range(len(queue)):
    print(queue[i], end=' ')