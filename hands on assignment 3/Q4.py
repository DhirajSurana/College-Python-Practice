
a=int (input("enter a"))
b=int (input("enter b"))
c=int (input("enter c"))
d=int (input("enter d"))
e=int (input("enter e"))
f=int (input("enter f"))
if(a*d-b*c)==0:
    print("the equation has no slolution")
else:
    x=(e*d-b*f)/(a*d-b*c)
    y=(a*f-e*c)/(a*d-b*c)
    print("x=",x,"y=",y)