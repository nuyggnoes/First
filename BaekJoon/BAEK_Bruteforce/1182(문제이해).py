import sys
n,s = map(int,sys.stdin.readline().split())
number = list(map(int,sys.stdin.readline().split()))
all_list = []
count = 0
for i in range(n+1):               #모든 경우의 수 저장
    for j in range(i+1,n+1):
        all_list.append(number[i:j])

for i in range(len(all_list)):      #각 경우의 수의 합과 s 비교
    x = sum(all_list[i])
    if x == s:
        count += 1
print(count)