import sys

n,m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
ans = -1

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s = card[i] + card[s] + card[k]
            if s > m:
                continue
            elif s < ans:
                continue
            elif s > ans and s <= m:
                ans = s
print(ans)