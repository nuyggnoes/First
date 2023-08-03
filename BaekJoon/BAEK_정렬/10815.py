import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int,input().split())))
M = int(input())
checks = list(map(int,input().split()))

for check in checks:
    low, high = 0, N-1
    flag = False
    while low<=high:
        mid = (low+high)//2
        if cards[mid] > check:
            high = mid - 1
        elif cards[mid] < check:
            low = mid + 1
        else:
            flag = True
            break
    print(1 if flag else 0, end = ' ')