import sys
p = [int(sys.stdin.readline()) for _ in range(9)]

for i in range(9):
	for j in range(i+1, 9):
		if (sum(p) - p[i] - p[j] == 100):
			del p[i]
			del p[j-1]
			break
	if len(p) == 7:
		break

for i in sorted(p):
	print(i)