n = int(input())
a = input()

colors = { 'B' : 0, 'R' : 0 } 
colors[a[0]] +=1 
for i in range(1, n): 
    if a[i] != a[i-1]:
        colors[a[i]]+=1

result = min(colors['B'], colors['R'])+1
print(result)