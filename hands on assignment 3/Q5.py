x=float(input("Enter x"))
y=float(input("Enter y"))
if(x>0 and y>0):
    print("1st quadrant")
elif(x<0 and y>0):
    print("2nd quadrant")
elif(x<0 and y<0):
    print("3rd quadrant")
elif(x>0 and y<0):
    print("4th quadrant")
elif (x==0):
    print("on y -axis")
elif (y==0):
    print("on x -axis")