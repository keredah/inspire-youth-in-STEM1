
# !user/bin/env/python3
# this is a single line comment
#python programm it illustrate assignment.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 22nd feb 2023
#file : assignment
#write a programm that solves quadratic equation.
#ax2 + bx + c = 0# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

