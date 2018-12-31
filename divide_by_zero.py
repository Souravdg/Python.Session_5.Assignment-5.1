#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
Problem Statement:
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
def div(num1,num2):
    res =num1/num2
    return (res)

try:
    #x=input("Enter the first number: ")
    #y=input("Enter the second number: ")
    #result = div(int(x),int(y))
    result = div(5,0)
    print("The result is %f" %(result))
except ZeroDivisionError as e:
    print("Handle run-time 'div by 0' error:", e)

