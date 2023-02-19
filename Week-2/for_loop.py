# for i in range (0,7):
#     print (i)
    
#part of code that runs continously
#-for loop
# do while (condition)
#while (condition) for
sum =0
for i in range (0,10):
    sum = sum + i
    

print (sum)
product = 1
for x in range (1,10):
    product = product * x
    print (product)
# Iterating over dictionary
print("Dictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))
    
# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
    
for letter in 'geeksforgeeks':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
 
print('Current Letter :', letter)

# Python Program to
# show range() basics
 
# printing a number
for i in range(10):
    print(i, end=" ")
 
# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
    sum = sum + i
print("\nSum of first 10 numbers :", sum)

# Python program to demonstrate
# for-else loop
 
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
 
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
 
# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
 
# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
 
# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),



fruits = ["apple", "orange", "kiwi"]
 
# Creating an iterator object
# from that iterable i.e fruits
iter_obj = iter(fruits)
 

fruits = ["apple", "orange", "kiwi"]
 
# Creating an iterator object
# from that iterable i.e fruits
iter_obj = iter(fruits)
 
# Infinite while loop
while True:
    try:
        # getting the next item
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
 
        # if StopIteration is raised,
        # break from loop
        break