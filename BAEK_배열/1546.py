N = int(input())
a = list(map(int,input().split()))
Max = max(a)
sum,result=0,0
for i in range(len(a)):
    a[i] = a[i]/Max*100
    sum += a[i]
result = sum / N
print(result)