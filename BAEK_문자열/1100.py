import sys
chess = []
count = 0
check = 1
for _ in range(8):
    a = list(sys.stdin.readline().rstrip())
    chess.append(a)

for i in chess:
    for j in i:
        check += 1
        if check % 2 == 0:
            if j == 'F':
                count += 1
    check += 1
print(count)