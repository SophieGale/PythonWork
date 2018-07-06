# Name    : 04Function
# Author  : John Merchant 
# Date    : 12 Jul 2016 
# Purpose : Example of function


file=open("filename.txt","r")

print("First line:")
print(file.readline())
file.seek(0)
print("First line again")
print(file.readline())

file.close()

