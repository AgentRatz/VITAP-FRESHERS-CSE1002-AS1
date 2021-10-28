# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:54:55 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Display Fibonacci Series Using While Loop

"""
 Fibonacci numbers, commonly denoted Fₙ, form a sequence, called the Fibonacci sequence,
 such that each number is the sum of the two preceding ones, starting from 0 and 1. 
 That is, and for n > 1. The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
 """
 

nterms = int(input("enter the nth term of the fibonacci series :- "))
n1, n2 = 0, 1 # given count to the first 2 terms
count = 0

# to check a number is a postive number and is valid
if nterms <= 0 :
    print ("Please enter a positve number ")
elif nterms == 1:
    print ("Fibonacci sequence upto" ,nterms,":")
    print(n1)
# to execute the fibonacci sequence
else: # this executes when it is false for all the above conditions
    print ("fibonacci series")
    while count < nterms:
        print (n1)
        nth = n1+n2
# updating the  values
        n1 = n2
        n2 = nth
        count += 1
