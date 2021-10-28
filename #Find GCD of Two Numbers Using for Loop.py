# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:28:53 2021

@author: 91798
"""
#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Find GCD of Two Numbers Using for Loop
"""
The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers 
is the largest positive integer that perfectly divides the two given numbers
For example, the H.C.F of 12 and 14 is 2.
"""
# this code is based on define function where x and y are input variables

def find_gcd(x,y): # give definition
    # choosing a small number first
    
    if x > y : 
        smaller = y
    else:
        smaller = x
    
    for i in range (1, smaller+1):
        if((x % i ==0) and ( y % i == 0 )) :
            gcd = i
        
    return gcd

num1 = int(input("enter the first number :- "))
num2 = int(input("enter a second number :- "))

print ("the GCD of ", num1, 'and',num2, 'is', find_gcd(num1,num2))


"""
this can also be done without using the def function 

num1 = int(input("enter the first number :- "))
num2 = int(input("enter a second number :- "))

if num1 > num2 : 
    smaller = num2
else:
    smaller = num1

for i in range (1, smaller+1):
    if((num1 % i  == 0) and ( num2 % i == 0 )) :
          gcd = i
print (gcd)

"""