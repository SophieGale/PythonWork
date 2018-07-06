# Name    : 09OptionalParametersProcedure
# Author  : John Merchant 
# Date    : 11 Jul 2016 
# Purpose : Exercise of procedure with optional parameters

def result(grade,score=50,feedback="Well Done!"):
    print("You scored",score,"which is a grade",grade,feedback)

result("C")
result("A",87)
result("E",12,"Must do Better!")
