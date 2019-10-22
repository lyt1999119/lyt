import math

def calc(a,b,c):
    key=b**2-4*a*c
    if key>0:
        x1=(-b+math.sqrt(key))/2*a
        x2=(-b-math.sqrt(key))/2*a
    if key==0:
        x1=-b/2*a
        x2=x1
    if key<0:
        print('方程无解‘）
        return(None,None)
    return(x1,x2)
print(calc(a,b,c))


    
        
