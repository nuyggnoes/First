# import sys
# input = sys.stdin.readline
# n,m = map(int, input().split())
# num = list(map(int, input().split()))

# def Q(arr,i,j,k):
#     arr = arr[i-1:j]
#     arr.sort()
#     return arr[k-1]

# for _ in range(m):
#     i,j,k = map(int, input().split())
#     print(Q(num,i,j,k))
# ----------------------------------------------------------------
#  시간초과
# ----------------------------------------------------------------

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
num = list(map(int, input().split()))

def Q(arr,i,j,k):
    arr = arr[i-1:j]
    arr.sort()
    return arr[k-1]

for _ in range(m):
    i,j,k = map(int, input().split())
    print(Q(num,i,j,k))