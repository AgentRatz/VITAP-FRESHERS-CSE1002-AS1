# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:48:15 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Print Multiplication Table Using for Loop

num = int(input("enter an integer :- ")) # take input from user

for i in range (1, 11): # itrate 10 times
    print (num,'X', i, '=', num*i )
    
    

"""
this can be prolonged when 
num = int(input("enter an integer :- ")) # take input from user
times = int(input('Please enter the nth number of the table u want :- '))

for i in range (1, times+1): # itrate 10 times
    print (num,'X', i, '=', num*i ) 
    
"""

    