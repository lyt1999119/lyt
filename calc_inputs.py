import math

def calc(a,b):
    return math.sqrt(a**2+b**2)

while 1:
    a,b=map(int,input('please input two integers:').split()) 
    print(calc(a,b))


    
        