n = int(input())
a = []
for i in range(1,n):
    value=0
    value += i
    k=value
    for j in str(k):
        value+=int(j)
    if value == n:
        a.append(k)
print(min(a))
