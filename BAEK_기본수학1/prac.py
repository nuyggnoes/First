from collections import deque
p = ['1','2','3','4']
p = deque(p)
p.popleft()
print(list(p))