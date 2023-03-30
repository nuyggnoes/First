N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    A,B = a,b
    while a != 0:
        b = b%a
        a,b = b,a
        print(a,b)
    print(A*B//b)