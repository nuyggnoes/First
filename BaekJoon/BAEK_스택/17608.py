import sys
n = int(sys.stdin.readline())
stack = []
bars = []
cnt = 1
for i in range(n):
    h = (int(sys.stdin.readline()))
    bars.append(h)
stack.append(bars.pop())
while True:
    if not bars : break
    if stack[-1] >= bars[-1]: bars.pop()
    else :
        stack.append(bars.pop())
        cnt += 1
print(cnt)