#A program that takes two given numbers and returns their LCM
#  -Shriram Krishnamachari 7/19/16

from collections import Counter as mset

def smallestFactor(n):
    for i in range(2, n+1):
        if n % i == 0:
             return i


def factorize(number):
    factor = list()
    if number == 1:
        factor.append(1)
    cn = number
    while cn > 1:
        sf = smallestFactor(cn)
        factor.append(sf)
        cn = cn / sf
        
    return factor
        
        
        


def gcd(number1, number2):

    factor1 = factorize(number1)
    
    factor2 = factorize(number2)
    
    commonfactors =  list((mset(factor1) & mset(factor2)).elements())
    
    gcd = 1
    # the following loop takes each element in common factors
    # and makes gcd = gcd * e
    # the short form of which is gcd *= e
    for e in commonfactors: 
      gcd *= e
    
    return gcd
    

def lcm(number1, number2):
    lcm = number1*number2/gcd(number1, number2)
    return lcm

number1 = input('Give a number')
number2 = input('Give another number')

print 'The Least common multiple is ' + str(lcm(number1, number2))