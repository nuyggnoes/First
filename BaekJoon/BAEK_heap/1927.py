import sys
import heapq
n = int(sys.stdin.readline())            #최소 힙
heap = []
for _ in range(n):
    ord = int(sys.stdin.readline())
    if ord:
        heapq.heappush(heap,ord)
    else:
        if not heap : print(0)
        else : print(heapq.heappop(heap))