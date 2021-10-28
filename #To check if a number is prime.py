#VITAP assignment-1
#School: SCOPE 
#Semester: Fall Sem 2021-22
#Subject: Problem Solving using Python 
#Subject Code: CSE1012
#Checking if a number is prime or not

num = int(input("Please enter an integer")) #To ask input
if num > 1: # to check if a number is postive integer

    for i in range (2,int(num/2)+1) : # To itrate from 2 to n/2
# if a number is divisible by 2 and n/2 then it is not prime

        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
    
    
    
    
    """
    # Python program to check if
# given number is prime or not
 
num = 11
 
# If given number is greater than 1
if num > 1:
 
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
 
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
 
else:
    print(num, "is not a prime number")
                                        """