n=list(range(1,10001))
x=[]
for i in range(1,10):
    n1=i+i
    x.append(n1)
for i in range(10,100):
    a=str(i)
    n2=i+int(a[0])+int(a[1])
    x.append(n2)
for i in range(100,1000):
    b=str(i)
    n3=i+int(b[0])+int(b[1])+int(b[2])
    x.append(n3)
for i in range(1000,10000):
    c=str(i)
    n4=i+int(c[0])+int(c[1])+int(c[2])+int(c[3])
    x.append(n4)
result=list(set(n)-set(x))
result.sort()
for i in result:
    print(i)