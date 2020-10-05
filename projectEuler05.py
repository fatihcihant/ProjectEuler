# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:47:25 2020

@author: fatih cihan
"""


"""
problem 5:
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

n = 2520
liste = [20,19,18,17,16,15,14,13,12,11]

while(True):
    
    for i in liste:
        if(n % i != 0):
            n += 1
            
            break
    else:
        print(n)
    
        break
                