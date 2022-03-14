import sys
n = int(sys.stdin.readline())
card = {}
rank = []
for _ in range(n):
    c = sys.stdin.readline().rstrip()
    if c in card:
        card[c] += 1
    else:
        card[c] = 1
print(card)
c = max(card.values())
for key,value in card.items():
    if c == value:
        rank.append(key)
rank.sort()
print(rank[0])