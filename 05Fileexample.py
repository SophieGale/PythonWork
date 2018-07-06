# Name    : 01FileWrite
# Author  : John Merchant 
# Date    : 12 Jul 2016 
# Purpose : Example to open and write to file

file = open("filename.txt","w")

for n in range(1,11):
    newline = "This is line " + str(n) + "\n"

    file.write(newline)

    file.close()

