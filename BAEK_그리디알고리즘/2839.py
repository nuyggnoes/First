kg = int(input())
a = 3
b = 5
def answer(a,b,kg):
    count,rest=divmod(kg,b)

    if count == 0:
        if rest % a != 0: return -1

    if rest == 0:
        return count
    
    if rest % a == 0:
        return count + 1
    
    for _ in range(5000):
        count -= 1
  
        if (rest + b) % a == 0:
            count += (rest+b) // a
            return count
        
        if count == 0:
           break
        
    return -1 
    
print(answer(a,b,kg))