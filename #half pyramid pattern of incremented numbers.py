# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:54:23 2021

@author: 91798
"""

#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
# Print the following Pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# half pyramid pattern of incremented numbers

rows = 5 #  here there are 5 rows so rows = 5
for i in range(0, rows): # itrate from 0 to rows 
    i += 1 # the index starts from 0 , here in question we want 1 to be printed first so we need to add +1 to i 
    for j in range (0, i):
        j += 1
        print(j, end= ' ') # to arrange with space we need to give an empty space string and ends with every j
    print('') # print is not inside the loop because we need to print evry value inside it 
    
""" 
we can do it directly by 
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
  """
"""
We can do the same pattern using the while loop
i = 0
while (i<=5):
     j = 1
     while(j<=i):
         print(j, end=" ")
         j +=1
     print()
     i += 1
"""
     
 