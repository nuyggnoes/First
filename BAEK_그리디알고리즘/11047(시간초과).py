n,k = map(int,input().split())
a = []
count = 0
i = 0
for i in range(n):
    i=int(input())
    a.append(i)

while k != 0:

    for i in range(n):
        if a[i] < k and a[i+1] > k:
            count += k // a[i]
            k = k % a[i]
print(count)