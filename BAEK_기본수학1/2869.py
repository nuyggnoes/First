import sys

a,b,v = map(int,sys.stdin.readline().split())
result = 0

if (v-a) > (a-b):
    if (v-a)%(a-b) == 0:
        result = (v-a) + (a-b)
    else:
        result = 1 + (v-a)//(a-b) + (v-a)%(a-b)
elif (v-a) < (a-b):
    result = (v-a) + 1
else:
    result = 1
print(result)