v = input()
a = []
b = []
c = []
for i in range(65,91):  # 대문자 개수
    a.append(v.count(chr(i)))
for i in range(97,123):  # 소문자 개수
    b.append(v.count(chr(i)))
for i in range(len(a)):  # a + b = 알파벳 개수
    c.append(a[i]+b[i])
M = max(c)  # 알파벳 사용 횟수 최댓값
if c.count(M) != 1 : result = '?'  # 최댓값이 1이 아니면 '?' 저장
else : result = chr(c.index(M)+65)  # 1일 경우 해당 알파벳 저장
print(result)