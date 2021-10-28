# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:42:36 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Print the following pattern (inverted half pyramid pattern with number)
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2 
# 1

rows = 5 # number of rows are 5 so rows = 5
for i in range(rows, 0, -1): # from rows to the -1th term with 0 step 
    for j in range(1,i+1): # itrate from 1 to 5 
        print(j, end=' ') # print with space
    print("") # print output
        