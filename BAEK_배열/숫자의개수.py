A=int(input())
B=int(input())
C=int(input())
result=A*B*C
a=list(map(int,str(result)))
for i in range(10):
    print(a.count(i))