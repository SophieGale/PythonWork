# Name    : 04Function
# Author  : John Merchant 
# Date    : 12 Jul 2016 
# Purpose : Example of function

 

def maximum(number1,number2):
    if number1 > number2:
        return number1
    else:
        return number2

number1 = float(input("Please enter first number : "))
number2 = float(input("Please enter second number : "))

print("Maximum is", maximum(number1,number2))
print("Maximum is", max(number1,number2))
