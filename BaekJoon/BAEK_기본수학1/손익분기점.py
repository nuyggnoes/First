a,b,c = map(int,input().split())
result = (a // (c-b) if c!=b else print(-1))
if result < 0 :
    print(-1)
else:
    print(result+1)