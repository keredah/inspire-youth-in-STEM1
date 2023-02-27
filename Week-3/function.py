# !user/bin/env/python3
# this is a single line comment
#python programm it illustrate how to use function.
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 23rd feb 2023
#file : function
#sets
my_fruits={"banana","oranges","mangoes","melon","pinaple"}
for fruit in my_fruits:
    print(len(my_fruits))
    print(type(my_fruits))
#fuctions are block of code excuted together
#users  key word def
def print_name():
    print ("my name is peter")
    print("im from nairibi")
    print("my hobbby is swimming")
#calling the function
#print_name
def add_num(num1,num2):
    sum_num = num1+num2
    print(sum_num)

add_num(30,20)
add_num(5,4)
add_num(2,6)

def mult_num(num1,num2):
    reslt = num1*num2
    print(reslt)
mult_num(2,4)
mult_num(4,7)

def sub_num(num1,num2):
    diff_num = num1-num2
    print(diff_num)
sub_num(5,2)
sub_num(9,7)

def div_num(num1,num2):
    quotient = num1/num2
    print(quotient)
div_num(6,2)
div_num(9,3)


#write a programm to print fuctorial of a number using function
#def fuctorial(n):