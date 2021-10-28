# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:35:27 2021

@author: 91798
"""
#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Find LCM of Two Numbers Using While Loop

"""
The least common multiple (L.C.M.) of two numbers is the smallest positive integer 
that is perfectly divisible by the two given numbers
"""
# this code is done using define function
def LCM(x,y):
# choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0 )) :
           lcm = greater
           break
       greater += 1
       
   return lcm

num1 = int(input("enter the first number :- "))
num2 = int(input("enter a second number :- "))

print ("The LCM of" , num1,"and", num2, "is" , LCM(num1,num2))

"""
This can be done without usinf the def function too 

num1 = int(input("enter the first number :- "))
num2 = int(input("enter a second number :- "))

if num1 > num2 : 
    greater = num1
else:
    greater = num2
while(True):
    if((greater % num1 == 0) and (greater % num2 == 0 )) :
        lcm = greater
        break
    greater += 1

    


print ("The LCM of" , num1,"and", num2, "is" ,lcm)
"""

    
    
    