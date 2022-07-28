#!/usr/bin/python3
# control structures  

Year = int(input("Please enter a year: "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("Dieses Jahr ist ein Schaltjahr")
        else:
            print("Dieses Jahr ist kein Schaltjahr")       
    else:
        print("Dieses Jahr ist ein Schaltjahr")
else:
    print("Dieses Jahr ist kein Schaltjahr")