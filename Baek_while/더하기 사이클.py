N = int(input())
temp = N
count = 1
if N >= 10:
    N = ((N//10) + (N%10)) % 10 + ((N%10)*10)
else:
    N = N*10 + N
while True:
    if N == temp:
        break
    elif N >= 10:
        N = ((N//10) + (N%10)) % 10 + ((N%10)*10)
    else:
        N = N*10 + N
    count += 1
print(count)