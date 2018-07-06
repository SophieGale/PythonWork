# Name    : 04Function
# Author  : John Merchant 
# Date    : 12 Jul 2016 
# Purpose : Example of function


file = open("filename.txt","r")

print("First line:")
print(file.readline())
print("Second line:")
print(file.readline())
print("Rest of line:")
print(file.read())
print("Blank line:")
print(file.readline())

file.close()
