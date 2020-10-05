"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
numbers=[]

for i in range(100,1000):
    for k in range(100,1000):
        numbers.append(i*k)


palindrome=[]

for num in numbers:
    if(len(str(num))==5):
        d1=num%10
        d2=int(num/10)%10
        d3=int(num/100)%10
        d4=int(num/1000)%10
        d5=int(num/10000)%10
        
        if(d5==d1 and d4==d2):
            palindrome.append(num)

    if(len(str(num))==6):
        d1=num%10
        d2=int(num/10)%10
        d3=int(num/100)%10
        d4=int(num/1000)%10
        d5=int(num/10000)%10
        d6=int(num/100000)%10
        
        if(d6==d1 and d5==d2 and d4==d3):
            palindrome.append(num)
print(max(palindrome))












        
        

        
        
        
        
