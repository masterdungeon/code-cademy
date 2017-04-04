import math
def is_prime(x):
    c=0
    if x<2:
        return False
    else:
        for i in range(1,x+1):
            if x%i==0:
                c+=1
        if c==2:        
            return True
        else:  
            return False
                