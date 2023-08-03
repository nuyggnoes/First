import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n = int(sys.stdin.readline())
    p = [sys.stdin.readline().rstrip() for _ in range(n)]
    p.sort()

    for i in range(n-1):
        l = len(p[i])
        if p[i] == p[i+1][:l]:
            print('NO')
            break  
    else: print('YES')