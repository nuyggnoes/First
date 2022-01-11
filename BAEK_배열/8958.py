N = int(input())
while True:
    N -= 1
    score = 0
    result = []
    a = input()
    result.append(a)
    n = a
    n_list = (n.split('X'))
    n_len = (len(n_list))
    print(n_len)
    for i in range(0,n_len):
        number = (n_list[i])
        number_len = len(number)
        for i in range(1,number_len+1):
            score += i        
    print(score)
    if N == 0:break