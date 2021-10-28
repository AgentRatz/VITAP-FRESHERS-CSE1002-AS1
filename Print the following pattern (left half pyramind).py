# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:15:29 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Print the following pattern (left half pyramind)
# *
# * *
# * * *
# * * * *
# * * * * *

n  = 5
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1
    
"""
this can also be done using the for loop
for i in range(0, num):
    for j in range(0, i+1):
        print("* ",end="")
    print("")
"""