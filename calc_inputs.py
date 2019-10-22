import math

def calc(a,b,c):
 if a != 0:
    key=b**2-4*a*c
    if key<0:
       print("无解")
    elif key==0:
        x1=-b/2*a
        x2=x1
        print("唯一根",x1)
    else:
        x1=(-b+math.sqrt(key))/2*a
        x2=(-b-math.sqrt(key))/2*a
        print("x1=",x1,"\t","x2=",x2)

    
        
