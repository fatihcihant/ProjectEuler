# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:00:21 2020

@author: fatih cihan
"""




def allprimes(n):
    """bir sayıdan küçük bütün asal sayıları dizi olarak döndüren fonksiyon"""
    primes = list(range(2,n+1,1))
    
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])
    
    
print(allprimes(2000000))
    

    
    
    
    













