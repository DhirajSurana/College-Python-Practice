
import random
user=int(input("Enter 0,1,2 scissor(0),rock(1),paper(2)"))
computer=random.randint(0,2)
if user==0 and computer==0:
    print("tie")
elif user==0 and computer==1:
    print("computer wins")
elif user==0 and computer==2:
    print("user wins")
elif user==1 and computer==0:
    print("user wins")
elif user==1 and computer==1:
    print("tie")
elif user==1 and computer==2:
    print("computer wins")
elif user==2 and computer==0:
    print("computer wins")
elif user==2 and computer==1:
    print("user wins")
elif user==2 and computer==2:
    print("tie")
else:
    print("invalid input")