H,M=map(int,input().split()) 
if M-45<0: 
    M=(60-45)+M   
    H-=1  
    if(H<0):  
        H+=24   
else:
    M-=45
print(H,M)