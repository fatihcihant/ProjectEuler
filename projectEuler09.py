# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:52:56 2020

@author: fatih cihan
"""

a, b, c = 0, 0, 0

for a in range(1,500):
    for b in range(a+1,500):
        c = 1000 -a -b
        
        if(a**2 + b**2 == c**2):
            print(a,b,c)