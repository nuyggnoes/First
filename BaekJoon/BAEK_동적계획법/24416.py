d = [0] * 41
cnt = 0
def fib1(n):
    if n == 1 or n == 2:
        return 1
    else : return (fib1(n-1)+fib1(n-2))

def fib2(n):
    global cnt
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    cnt += 1
    d[n] = fib2(n-2) + fib2(n-1)
    return d[n]

n = int(input())
fib2(n)
print(fib1(n),cnt)