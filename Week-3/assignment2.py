# !user/bin/env/python3
# this is a single line comment
#python programm assignment.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 20th feb 2023
#file : assignment
#using a for loop draw a diamond
#using a for loop draw a diamond

word=input("Enter characters: ")
length=input()
for i in range (0, length):
    for j in range(length-i-1):
        print(' ', end="")
    for j in range(0, i+1):
        print(word[j], end="")
    for k in range (i-1, -1, -1):
        print (word[k], end="")
    print()
for l in range (1,length):
    for j in range(l) :
        print(' ', end="")
    for m in range (0,length-l-1):
        print(word[m], end ="")
    for n in range (length-l-1,-1,-1):
        print(word[n], end="")
    print()
