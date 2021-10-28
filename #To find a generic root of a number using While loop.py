# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:27:26 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#To find a generic root of a number using While loop

""" 
genric root is the sum of the numbers to reduce it below 10 
for example if the number is 2259 your answer should be 2+2+5+9 = 18 = 1+8 = 9
therefore 9 is the genric root of 2259"""

num= int(input('enter a number')) # take an input from user

while num > 10  :
    tot=0
    sum = 0
    while num :
        total=num % 10
        num= num // 10
        sum+= total
    if sum > 10 :
        num = sum
    else:
        break
print("genric root is ", int(sum))


""" this can also be done using single line method 
num = 2259
generic_root = 1 + ((num - 1) % 9)
  
print("generic root = ", generic_root) """


    