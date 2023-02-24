# !user/bin/env/python3
# this is a single line comment
#python programm it illustrate advanced data types
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 20th feb 2023
#file : advanced data types

# advanced data_ types
#mutable vs imutabe
#add/remove elements
#immutable ------>data types
#list(immutable)
friends=["jade","anita","mary"]
#or friends=[]for empty
#add---->append(),extend()
#remove------>del()pop()
students=["marcy","margy","methlet"]
friends.extend(students)
friends.append("jade")
friends.sort()
#tuples(immutable)
#type are unchangeable
stationaries=("ruler","pen","book")
for stationary in stationaries:
    print (stationary)
numbers=(1,2,3,4,5,6,7,)
#key and key value
students ={"name":"john","age":24,"gender":"male"}
print(students["name"])
print(students["age"]) 
print(students["gender"])
friends={"fevourite_colour":"pink","hobby":"reading","team":"manuted","course":"IT","weight":56,"height":6.1}
print(friends["fevourite_colour"])
print(friends["hobby"])
print(friends["course"])
print(friends["team"])
print(friends["weight"])
print(friends["height"])
