
# !user/bin/env/python3
# this is a single line comment
# Assignment
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 20th feb 2023
#file : assignment
#using a for loop draw a triangle
rows= int(input("enter alphabet pattern Rows"))
print("====print triangle alphabet pattern")
for i in range(0,rows):
    alphabet=65
    for j in range (rows,i-1):
        print(end='')
    for k in range(0,1+1):
        print('%c'%(alphabet +k),end='')
        print()    
        print("triangle alphabet pattern")