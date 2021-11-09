Rahul=int(input("Enter age of Rahul"))
Ayush=int(input("Enter age of Ayush"))
Ajay=int(input("Enter age of Ajay"))
if Rahul>Ayush and Rahul>Ajay:
    print("Rahul is eldest")
elif Ayush>Rahul and Ayush>Ajay:
    print("Ayush is eldest")
elif Ajay>Rahul and Ajay>Ayush:
    print("Ajay is eldest")
else:
    print("All are same age")