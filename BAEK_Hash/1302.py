import sys
n = int(sys.stdin.readline())
li = dict()
rank = []
for _ in range(n):
    book = sys.stdin.readline().rstrip()
    if book not in li:
        li[book] = 1
    else:
        li[book] += 1
book = max(li.values())

for key,value in li.items():
    if book == value:
        rank.append(key)
rank.sort()
print(rank[0])