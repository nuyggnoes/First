import sys

s = list(sys.stdin.readline().rstrip())

while True:
    if len(s)>10:
        a = s[:10]
        x = ''.join(a)
        print(x)
        s = s[10:]
    else:
        print(''.join(s))
        break