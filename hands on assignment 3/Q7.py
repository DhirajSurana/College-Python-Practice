
year=int (input("Enter the year: "))
leapyear=False
if year%4==0:
    if year%100==0:
        if year%400==0:
            leapyear=True
        else:
            leapyear=False
    else:
        leapyear=True
month=int (input("Enter the month: "))
if month==1:
    print("january ",year,"has 31 days")
elif month==2:
    if(leapyear):
        print("february ",year,"has 29 days")
    else:
        print("february ",year,"has 28 days")
elif month==3:
    print("march ",year,"has 31 days")
elif month==4:
    print("april ",year,"has 30 days")
elif month==5:
    print("may ",year,"has 31 days")
elif month==6:
    print("june ",year,"has 30 days")
elif month==7:
    print("july ",year,"has 31 days")
elif month==8:
    print("august ",year,"has 31 days")
elif month==9:
    print("september ",year,"has 30 days")
elif month==10:
    print("october ",year,"has 31 days")
elif month==11:
    print("november ",year,"has 30 days")
elif month==12:
    print("december ",year,"has 31 days")
else:
    print("Invalid month")
