# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:33:25 2021

@author: 91798
"""
#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#To reverse a number using while loop

num = int(input("Enter a number which u want to get reversed :- ")) #to ask input from user
reversed_num = 0 

while num>=1:
    digit = num % 10 # input's remainder when divided by 10 gives the last digit
    reversed_num = reversed_num * 10 + digit  # " LOGIC " 
    num //= 10 # gives the numbers other than the decimal part
print("Reversed Number: " + str(reversed_num))


"""
can also be done using string slicing 
num = 123456
print(str(num)[::-1])
"""
