# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:45:19 2020

@author: fatih cihan
"""
a, b = 1, 1
c = 0
count = 2
while(len(str(c)) < 1000):
    c = a + b
    a = b
    b = c
    count += 1
print(count)
