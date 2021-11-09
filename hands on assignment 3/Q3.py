a=int(input ("Enter a"))
b=int(input ("Enter b"))
c=int(input ("Enter c"))
d=pow((b*b-4*a*c),0.5)
if d>0:
    x1=(-b+d)/2*a 
    x2=(-b-d)/2*a
    print("x1=",x1)
    print("x2=",x2)
elif d==0:
    print("Roots are real and equal")
    print((-b+d)/2*a)
else:
    print("Roots are imaginary")
