# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:48:40 2020

@author: fatih cihan
"""

sum1 = 0
sum2 = 0

for i in range(1,101):
    sum1 += i**2
    sum2 += i
print(sum2**2 - sum1)