# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:18:29 2021

@author: 91798
"""
#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Print the following pattern (downward pyramid pattern of stars)

# * * * * *
# * * * *
# * * *
# * *
# *
rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")