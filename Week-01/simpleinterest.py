# !user/bin/env/python3
# this is a single line comment
#python programm it illustrate how to calculate simplie interest.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 08th feb 2023
#file : operators

# write a programm that calculate simple interest
p = input ("enter principal amount:")
r = input ("enter the rate :")
t = input ("enter the time duration :")
simple_interest  = ( int(p) * int(r)* int(t)) /100
print (" simple interest is :", simple_interest)
#calculating surface area of a sphere
pi = 3.142
r =  input("enter the redius:")
sa = ((pi) * 4 * int(r) * int(r))
print ("surface area :",sa)
#calculating surface area a cylinder
pi = 3.142
r  = input (" enter the radius :")
d = input (" enter the diameter :")
h = input (" enter the hieght:")
sa = ( (pi) *2 * int( r) * int(r) + (pi) *int(d) *int(h))
print ( "surface area:",sa)
#culculating volume of a sphere
pi = 3.142
r =  input(" enter radius")
vs = ((4/3) * (pi) * int (r) * int (r))
print ( "volume of the sphere ", vs)
#culculating the volume of a cylinder
pi = 3.142
r =input ("enter the radius")
h =input ("enter the height")
vc = ( (pi) * int(r) * int(r) * int(h))
print ("volume of a cylinder",vc)
