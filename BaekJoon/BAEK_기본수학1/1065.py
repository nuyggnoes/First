import sys

n = int(sys.stdin.readline())
count = 0

if n > 99:
    count = 99
    for i in range(100, n+1):
        x = i // 100
        y = (i % 100) // 10
        z = i % 10
        if (z - y) - (y - x) == 0:
            count += 1
    print(count)
else:
    print(n)