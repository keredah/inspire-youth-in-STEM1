# !user/bin/env/python3
# this is a single line comment
#python programm it illustrate how to use"if" and "elif".
# name = peter keredah
# email =peterkeredah85@gmail.com
# date: 13th feb 2023
#file : conditions

# write a programm tha calculate 16%tax on income raanging between 100-150k
#19%tax if income is between 150-300k
#30% tax if income is above 300k
#5%if the income is less 100k
#print gross income,net income.
gross_income=int(input("enter your net income"))
if gross_income<100000 :
    net = gross_income - (gross_income *0.05)
elif((gross_income > 100000) & (gross_income <= 150000)):
    net = gross_income - (gross_income*0.16)
elif((gross_income > 150000) & (gross_income <= 300000)):
     net = gross_income - (gross_income*0.19)
elif(gross_income >300000):
    net = gross_income - (gross_income*0.3)
print(gross_income)
print(net)