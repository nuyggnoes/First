import sys
input = sys.stdin.readline
N = int(input())
mem = {}

for _ in range(N):
    name,exist = input().split()
    if exist == 'enter':
        mem[name] = exist
    else:
        del mem[name]

mem = sorted(mem.keys(), reverse=True)

for i in mem:
    print(i)
