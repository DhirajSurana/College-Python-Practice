x=float(input("enter x"))
y=float(input("enter y"))
length=pow((x*x+y*y),0.5)
if(length<10):
    print("point is inside the circle")
elif(length==10):
    print("point is on the circle")
else:
    print("point is outside the circle")