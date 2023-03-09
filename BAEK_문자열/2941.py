from curses.ascii import isalpha


alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
S = input()
result = 0
for i in alpha:
    if i in S:
        S = S.replace(i,"?")
        result += 1
for i in S:
    if isalpha(i):
        result += 1
print(result)