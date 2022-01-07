a=[]
for i in range(9):
    x=int(input())
    a.append(x)
Max=max(a)
Max_index=a.index(Max)+1
print(Max)
print(Max_index)