#Name: 02IfElifElse
#Author: John Merchant
#Date: 08 Jul 2016
#Purpose: Example of if/elif/elif/else

mark = int(input("Enter mark: "))

if mark > 85:
    print("Distinction")

elif mark > 75:
    print("Merit")

elif mark > 65:
    print("Pass")
    
else:
    print("Fail")
    
