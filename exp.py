def exp(x,y):
    a=1
    b=0
    while(b < y):
        a=a*x
        b=b+1
    return a

z=exp(2,3)
print(z)