n = int(input())
p = list(map(int,input().split()))
sum=0
sum1=0
p1=[]
p.sort()
for i in p:
    sum += i
    p1.append(sum)
for i in p1:
    sum1 += i
print(sum1)