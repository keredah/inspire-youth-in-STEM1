
# !user/bin/env/python3
# this is a single line comment
# assignment.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 20th feb 2023
#file : assignment1

#create alist an empty list of musicians and add 3 musicians
#using for loo add 5 musicians
#copy to a new list called "select"
#pop out two celeb
#count out the remaining celeb.
musicians=[]
n=int(input("enter the nurmber of names required"))
for i in range (0,n):
    elem=str(input("enter the namesof the muscians:"))
    musicians.append(elem)
print("the created list of names",musicians)
celebs=musicians.copy()
print (celebs)
celebs.sort()
print(celebs)
celebs.pop(2)
print(celebs)

