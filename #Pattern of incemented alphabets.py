# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:19:38 2021

@author: 91798
"""
#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
# Print the following Pattern
# A
# B B
# C C C
# D D D D
# E E E E E 
# Pattern of incemented alphabets

# we have to use chr function to do this problem

for i in range (65,70): # According to ASCII table code Alpabets go from 65 - so on 
# here chr(65) is 'A' and chr(70) is 'E'
    for j in range(65,i+1): # we have to use nested for in loop 
        print(chr(i), end = " ")
    print ()
    