n = int(input())
e = [i for i in range(666,n*1000) if str(i).count('666') == 1 or str(i).count('666') == 2]
print(e[n-1])