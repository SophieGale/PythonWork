#Name: 06IfNested
#Author: John Merchant
#Date: 08 Jul 2016
#Purpose: Example of nested if

print("Menu")
print("3 - Level 3")
print("4 - Level 4")

examlevel = int(input("Enter exam level: "))

if examlevel == 3:
    mark = int(input("Enter level 3 mark: "))

    if mark > 65:
        print("Pass")

    else:
        print("Fail")

elif examlevel == 4:
        mark = int(input("Enter level 4 mark: "))

        if mark > 50:
            print("Pass")

        else:
            print("Fail")
    else:
         print("Invalid Level")
            
         
        
