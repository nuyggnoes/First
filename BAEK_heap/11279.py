import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    ord = int(sys.stdin.readline())
    if ord:
        heapq.heappush(heap,-ord)
    else:
        if not heap : print(0)
        else : print(abs(heapq.heappop(heap)))