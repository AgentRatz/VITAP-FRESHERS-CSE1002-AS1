# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:58:09 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Print Factors of a Number

num = int(input("Enter a number :- ")) # take input from user
print ("The factors of " , num, 'are') # giving heading
for i in range(1,num+1): # for i in range from 1 to number+ 1 because indexing starts from 0
    if num % i == 0: # the range of numbers should give remainder 0 when divinded with the num
        factors = i # i is given a variable factors 
        print(factors) # given output print as factors
        

"""
this can be done using def method too 
# This function computes the factor of the argument passed
num = int(input("Enter a number :- ")) # take input from user
def print_factors(num):
   print("The factors of",num,"are:")
   for i in range(1, num + 1):
       if num % i == 0:
           print(i)
print_factors(num)
             
"""