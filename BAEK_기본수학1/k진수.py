def is_prime(n):  
    import math
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def make_n_mod(n, k):  
    j = ''
    while n > 0 :
        n, mod = divmod(n, k)
        j += str(mod)
    return j[::-1]
       
def solution(n, k):
    result1 = make_n_mod(n, k)
    s=result1.split('0')
    count = 0

    for i in s:
        # if i.isdigit():
        #     if is_prime(int(i)): 
        #         count += 1
        if i.isdigit() and is_prime(int(i)):
            count += 1
    return count

print(solution(110011, 10))