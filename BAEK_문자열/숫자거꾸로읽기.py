a,b=input().split()
a=list(a)
b=list(b)
n1=(int(a.pop())*100)+(int(a.pop())*10)+(int(a.pop()))
n2=(int(b.pop())*100)+(int(b.pop())*10)+(int(b.pop()))
print(n1 if n1>n2 else n2)