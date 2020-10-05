"""
problem:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def primeControl(number):
    for i in range(2,int(number/2+1)):
        if(number%i==0):
            return 0
    return 1


primeTemp=0
for k in range(2,600851475143):
    if(k%2==0):
        continue
    if(k%3==0):
        continue
    if(k%5==0):
        continue
    if(k%7==0):
        continue    
    if(primeControl(k)==1):
        primeTemp=k
print(primeTemp)
