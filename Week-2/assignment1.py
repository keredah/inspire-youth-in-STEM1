# !user/bin/env/python3
# this is a single line comment
#python programm it illustrate how to use for_loop.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 13th feb 2023
#file : assignment1

# write a program to calculate arithmetic prograssion of nurmbers between 1-100
sum= 0
for x in range (0,100):
    sum =sum + x
    print (sum)

#write a programm to list all even nurmbers
print("even nurmbers from 1 to 100")
for x in range (1,101) :
    if x % 2== 0 :
        print (x)

 #write a program of a list of all odd nurmbers
print("odd nurnmders from 1 to 100")
for y in range (1,100+1) :
    if y%2 == 1 : 
        print(y)

