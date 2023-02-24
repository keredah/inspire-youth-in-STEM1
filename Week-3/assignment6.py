
# !user/bin/env/python3
# this is a single line comment
#assignment.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 23nd feb 2023
#file : assignment
#write a factorial of a number using function
num =int(input("enter a number"))
factorial=1
if num<0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial=factorial*i
print("the factorial of",num,"is",factorial)