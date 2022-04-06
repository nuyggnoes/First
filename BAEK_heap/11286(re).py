import sys
import heapq
n = int(sys.stdin.readline())            #절댓값 힙
heap = []
for _ in range(n):
    ord = int(sys.stdin.readline())
    if ord:
        heapq.heappush(heap,(abs(ord),ord))
    else:
        if not heap : print(0)
        else: print(heapq.heappop(heap)[1])
    print(heap)