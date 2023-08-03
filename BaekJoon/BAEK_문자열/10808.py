import sys

n = sys.stdin.readline().rstrip()
result = []
for i in range(97,123):
    if n.count(chr(i)) != 0 :
        result.append(n.count(chr(i)))
    else :
        result.append(0)

for i in range(len(result)):  # 조심 
    result[i]=str(result[i])

print(' '.join(result))