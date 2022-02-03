import sys
from collections import deque
n = int(sys.stdin.readline())
number = deque(range(1, n + 1))


while len(number) > 1:
     number.popleft()
     number.append(number.popleft())

print(number[0])