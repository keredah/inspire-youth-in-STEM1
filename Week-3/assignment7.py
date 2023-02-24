#write a programm to calculate simple interest.
# !user/bin/env/python3
# this is a single line comment
#python programm assignment.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 23nd feb 2023
#file : assignment

# Python3 program to find simple interest
#  principal amount, time and
# rate of interest taken from user.
 
 
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
     
     
# Driver code
P = int(input("Enter the principle amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simple_interest(P,T,R)