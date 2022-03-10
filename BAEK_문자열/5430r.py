for _ in range(int(input())):
    f=list(map(len,input().replace('RR','').split('R')))
    n=int(input())
    print(f)
    a=input()[1:-1].split(',')
    s,e=sum(f[0::2]),n-sum(f[1::2])
    print(s,e)
    a=a[s:e] if len(f)%2==1 else a[s:e][::-1]
    print(f"[{','.join(a)}]" if s<=e else "error")