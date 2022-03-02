import sys
flag = True
while True:
    flag = True
    n = sys.stdin.readline().rstrip()
    if n == '0' : break
    for i in range(len(n)//2):
        if n[i] == n[len(n)-(i+1)]:
            continue
        else:
            flag = False
            break
    if flag: print('yes')
    else : print('no')