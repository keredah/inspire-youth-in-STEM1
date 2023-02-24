# !user/bin/env/python3
# this is a single line comment
#python programm it illustrate how to use"if" and "elif".
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 17th feb 2023
#file : numbers
# Get the average of the nurmbers in the list by first entering them as input 
#numbers=[]
n = int(input("Enter the number of elements: ")) 
for i in range(0, n): 
    elem = int(input("Enter the elements: ")) 
    numbers.append(elem) 
avg = sum(numbers)/n
print("The created list:",numbers)
print("The average = ",avg)