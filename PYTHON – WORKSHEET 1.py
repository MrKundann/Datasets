#!/usr/bin/env python
# coding: utf-8

# # ##
# ...
# ...
#                            PYTHON – WORKSHEET 1
# 
# Q1 to Q8 have only one correct answer. Choose the correct option to answer your question.
# 
# 1.Which of the following operators is used to calculate remainder in a division?
# A) #        B) &
# C) %        D) $                      
#         Ans: C) % 
# 
# 2. In python 2//3 is equal to?
# A) 0.666    B) 0
# C) 1        D) 0.67
#        Ans: B) 0
# 
# 3. In python, 6<<2 is equal to?
# A) 36 B) 10
# C) 24 D) 45
#        Ans: C) 24
# 
# 4. In python, 6&2 will give which of the following as output?
# A) 2 B) True
# C) False D) 0
#        Ans: A) 2 
# 
# 5. In python, 6|2 will give which of the following as output?
# A) 2 B) 4
# C) 0 D) 6
#        Ans: D) 6 
# 
# 6. What does the finally keyword denotes in python 
# A) It is used to mark the end of the code
# B) It encloses the lines of code which will be executed if any error occurs while executing the lines of code in 
# the try block.
# C) the finally block will be executed no matter if the try block raises an error or not.
# D) None of the above
#        Ans: C) the finally block will be executed no matter if the try block raises an error or not.
#   
# 7. What does raise keyword is used for in python?
# A) It is used to raise an exception.  B) It is used to define lambda function
# C) it's not a keyword in python.      D) None of the above
#        Ans: A) It is used to raise an exception.
# 
# 8. Which of the following is a common use case of yield keyword in python?
# A) in defining an iterator            B) while defining a lambda function
# C) in defining a generator            D) in for loop.
#        Ans: C) In Defining a generator.
# 
# Q9 and Q10 have multiple correct answers. Choose all the correct options to answer your question.
# 9. Which of the following are the valid variable names?
# A) _abc      B) 1abc
# C) abc2      D) None of the above
#        
#        Ans: A) _abc and  C) abc2 
# 
# 10. Which of the following are the keywords in python?
# A) yield     B) raise
# C) look-in   D) all of the above
#        
#         Ans: A) yield and B) raise. 
# ...
# 





11. Write a python program to find the factorial of a number.

# In[2]:

num = int(input("Enter any number :"))
fact = 1 
for i in range(1,num+1):
    fact = fact*i
print(fact)


12. Write a python program to find whether a number is prime or composite.

# In[ ]:

num = int(input("Enter any number :"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num,"is a composite number")
            break
    else:
        print(num,"is prime number")
elif num == 0 or 1: 
    print(num, "is neither prime number nor a composite number")
else: 
    print(num,"is a prime number")


13. Write a python program to check whether a given string is palindrome or not.

# In[ ]:

my_str = input("Enter string:")
if(my_str == my_str[::-1]):
   print("The string is a palindrome")
else:
   print("The string isn't a palindrome")



# # 14. Write a Python program to get the third side of right-angled triangle from two given sides.

# In[ ]:

a = int(input("Enter first side :"))
b = int(input("Enter second side :"))

from math import sqrt

c = sqrt(a**2 + b**2)
print("The length of third side is:", c)



# # 15. Write a python program to print the frequency of each of the characters present in a given string.

# In[ ]:


str1 = input("Inter the string:")
char = dict()
for i in str1:
    char[i] = char.get(i, 0) + 1
print (char)





# ## 15. Write a python program to print the frequency of each of the characters present in a given string

# In[ ]:

str1 = input("Inter the string:")
ch = dict()
for i in str1:
    ch[i] = ch.get(i, 0) + 1
print (ch)









