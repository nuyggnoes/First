import sys
n,m = map(int,sys.stdin.readline().split())
pocketmon_list = dict()

for i in range(1,n + 1):
    pocktmon = sys.stdin.readline().rstrip()
    pocketmon_list[pocktmon] = str(i)
    pocketmon_list[str(i)] = pocktmon

for _ in range(m):
    print(pocketmon_list[sys.stdin.readline().rstrip()])