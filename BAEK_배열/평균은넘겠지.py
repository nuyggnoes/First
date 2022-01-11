C=int(input())
while True:
    count = 0
    n=list(map(int,input().split()))
    for i in n:
        sum = 0
        sum += i
        avg = sum/(len(n)-1)
    for i in n:
        if i > avg:
            count += 1
    result = (count/(len(n)-1)) * 100
    print(result)
    C -= 1
    if C == 0:break