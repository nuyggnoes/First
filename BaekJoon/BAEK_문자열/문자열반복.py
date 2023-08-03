Test=int(input())
for i in range(Test):
    a,b=input().split()
    for i in b:
        print(int(a)*i,end="")
    print("")
