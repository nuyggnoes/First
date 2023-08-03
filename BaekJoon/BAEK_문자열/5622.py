alpha = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S = input()
result = 0
for i in range(len(S)):
    for j in alpha:
        if S[i] in j:
            result += alpha.index(j)+3
print(result)