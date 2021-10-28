# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:01:11 2021

@author: Rahul Bharadwaj
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Program to Check a Number is Palindrome or Not Using While Loop

num = int(input("enter a number:-"))
temp = num
rev = 0
while(num>0):
    dig = num%10
    rev = rev*10+dig
    num=num//10

if(temp == rev):
    print(temp, " is a palindrome!")

else:
    print(temp, "is not a palindrome!")


"""
This can be also done using the string slicing method 

num = input("Enter a number")
if num == num[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")

"""