# Get the average of the nurmbers in the list by first entering them as input 
#numbers=[]
n = int(input("Enter the number of elements: ")) 
for i in range(0, n): 
    elem = int(input("Enter the elements: ")) 
    numbers.append(elem) 
avg = sum(numbers)/n
print("The created list:",numbers)
print("The average = ",avg)