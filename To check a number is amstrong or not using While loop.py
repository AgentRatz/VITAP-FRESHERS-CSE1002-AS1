# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:38:06 2021

@author: Rahul Bharadwaj
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
# To check a number is amstrong or not using While loop
"""
An Armstrong number of three digits is an integer such that
 the sum of the cubes of its digits is equal to the number itself.
 For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371 
"""

num = int(input("enter a number :- ")) # Take input from user
sum = 0 # initailize sum 

# to find the sum of cube of each digit
temp = num
while temp > 0 :
    digit = temp % 10
    sum += digit**3
    temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
    

"""
Few of the 3 digit amstrong numbers are 
 153, 370, 371 and 407

"""
