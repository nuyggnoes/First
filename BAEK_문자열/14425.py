import sys
input = sys.stdin.readline

N,M = map(int,input().split())

S = {}
cnt = 0

for i in range(N):
    s1 = input().rstrip()
    S[s1] = True

for j in range(M):
    s2 = input().rstrip()
    if s2 in S:
        cnt += 1
print(cnt)