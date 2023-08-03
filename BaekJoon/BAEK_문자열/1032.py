n = int(input())
m = list(input())
l = len(m)
for _ in range(n-1):
    o = list(input())
    for i in range(l):
        if m[i] != o[i]:
            m[i] = '?'
print(''.join(m))