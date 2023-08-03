import sys
a,b,v = map(int,sys.stdin.readline().split())
print((v-b)//(a-b) if not (v-b)%(a-b) else (v-b)//(a-b)+1)