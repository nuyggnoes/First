import sys

def prime_n(x):
    if x == 1 :
        return False
    elif x == 2:
        return True
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
count = 0

for i in a:
    if  prime_n(i):
        count += 1
print(count)