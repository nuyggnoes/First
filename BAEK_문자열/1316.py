import sys
input = sys.stdin.readline
n = int(input())
group_check = n
for _ in range(n):
    word = input().rstrip()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            group_check -= 1
            break
print(group_check)