import itertools

n = int(input())
number = list(map(int,input().split()))
oper = list(map(int,input().split()))
ch_oper = ['+','-','*','//']       #연산자 저장
new_oper = []
result = []
for i in range(len(oper)):    #연산자 갯수 파악
    if oper[i] == 0:
        continue
    else : new_oper.append(oper[i]*ch_oper[i])
all_list = list(itertools.permutations(new_oper, n-1))
print(all_list)