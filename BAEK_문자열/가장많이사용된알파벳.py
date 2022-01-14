v = input()
a = []
b = []
c = []
for i in range(65,91):
    a.append(v.count(chr(i)))
for i in range(97,123):
    b.append(v.count(chr(i)))
for i in range(len(a)):
    c.append(a[i]+b[i])
M = max(c)
if c.count(M) != 1 : result = '?'
else : result = chr(c.index(M)+65)
print(result)