# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:42:58 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Program to Count Number of Digits of a Number (Integer) using While loop

num = int(input("Enter a number"))
copy_num = num
count = 0

while num != 0: # while number is not equal to zero
    num//= 10
    count += 1 
print ("the number of digits in", copy_num, "is", str(count))


"""
This can be also done by 
num = int(input("Enter a number"))
print (len(str(num)))

"""

"""
This can be alsso done by

import math
count = 0
num = int(input("Enter a number"))
count=log10.(n)+1
print ("the number of digits in ", num 'is', count)
"""