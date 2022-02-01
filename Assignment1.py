#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Que 1
'''Write a Python program to get the Fibonacci series between 0 to 50



Note : The Fibonacci Sequence is the series of numbers :

0, 1, 1, 2, 3, 5, 8, 13, 21, ....

Every next number is found by adding up the two numbers before it.

Expected Output : 1 1 2 3 5 8 13 21 34 '''

#answer1 *****************

n = int(input("enter:"))
a =1
b =0
total =1
while(total <= n) :
    print(total,end=" ")
    a=b
    b=total
    total=a+b
    
#***********************    

#Que 2
'''Write a Python program that accepts a word from the user and reverse it.



Sample Test Case



Input : Edyoda

output: adoydE '''

#answer2 *****************

a = "Edyoda"[::-1]
print(a)

#***********************    

#Que 3
''' Write a Python program to count the number of even and odd numbers from a series of numbers.



Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 5

Number of odd numbers : 4 '''

#answer3 *****************


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#***********************    

